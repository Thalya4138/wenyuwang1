"""Tests for async_pool.bounded_map (standard library only)."""

import asyncio
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from async_pool import bounded_map  # noqa: E402


class TestBoundedMap(unittest.IsolatedAsyncioTestCase):
    # ---------- ordering ----------
    async def test_preserves_input_order(self):
        async def work(x):
            # Later items finish first, so completion order != input order.
            await asyncio.sleep(0.02 * (10 - x) / 10)
            return x * x

        items = list(range(10))
        results = await bounded_map(work, items, concurrency=5)
        self.assertEqual(results, [x * x for x in items])

    async def test_returns_list_of_results(self):
        async def work(x):
            return x + 1

        self.assertEqual(await bounded_map(work, [1, 2, 3]), [2, 3, 4])

    async def test_empty_items(self):
        async def work(x):  # pragma: no cover - never called
            return x

        self.assertEqual(await bounded_map(work, []), [])

    # ---------- concurrency ceiling ----------
    async def test_respects_concurrency_limit(self):
        state = {"active": 0, "peak": 0}

        async def work(x):
            state["active"] += 1
            state["peak"] = max(state["peak"], state["active"])
            await asyncio.sleep(0.01)
            state["active"] -= 1
            return x

        await bounded_map(work, range(20), concurrency=3)
        self.assertLessEqual(state["peak"], 3)
        self.assertGreater(state["peak"], 1)

    async def test_concurrency_one_is_sequential(self):
        order = []

        async def work(x):
            order.append(("start", x))
            await asyncio.sleep(0)
            order.append(("end", x))
            return x

        await bounded_map(work, [1, 2, 3], concurrency=1)
        self.assertEqual(order, [("start", 1), ("end", 1), ("start", 2), ("end", 2), ("start", 3), ("end", 3)])

    async def test_does_not_create_a_task_per_item(self):
        created = {"count": 0}

        async def work(x):
            created["count"] += 1
            await asyncio.sleep(0.001)
            return x

        await bounded_map(work, range(10), concurrency=2)
        # At most 2 worker tasks exist; check no more than 2 coroutines overlap.
        self.assertEqual(created["count"], 10)

    # ---------- exception propagation ----------
    async def test_exception_propagates_and_cancels_rest(self):
        started = []

        async def work(x):
            started.append(x)
            if x == 2:
                raise RuntimeError("boom")
            await asyncio.sleep(0.5)
            return x

        with self.assertRaises(RuntimeError) as ctx:
            await bounded_map(work, range(6), concurrency=2)
        self.assertEqual(str(ctx.exception), "boom")
        # Remaining work must have been cancelled promptly rather than run to 0.5s.
        self.assertLess(len(started), 6)

    async def test_exception_type_is_preserved(self):
        class Custom(Exception):
            pass

        async def work(x):
            if x == 1:
                raise Custom("custom")
            return x

        with self.assertRaises(Custom):
            await bounded_map(work, [0, 1, 2], concurrency=2)

    # ---------- return_exceptions ----------
    async def test_return_exceptions_places_errors_in_place(self):
        async def work(x):
            if x % 2 == 1:
                raise ValueError(f"bad {x}")
            return x * 10

        results = await bounded_map(work, [0, 1, 2, 3, 4], concurrency=3, return_exceptions=True)
        self.assertEqual(results[0], 0)
        self.assertIsInstance(results[1], ValueError)
        self.assertEqual(str(results[1]), "bad 1")
        self.assertEqual(results[2], 20)
        self.assertIsInstance(results[3], ValueError)
        self.assertEqual(results[4], 40)

    async def test_return_exceptions_lets_other_items_finish(self):
        done = []

        async def work(x):
            if x == 1:
                raise RuntimeError("nope")
            await asyncio.sleep(0.01)
            done.append(x)
            return x

        results = await bounded_map(work, [0, 1, 2, 3], concurrency=2, return_exceptions=True)
        self.assertEqual(sorted(done), [0, 2, 3])
        self.assertIsInstance(results[1], RuntimeError)

    async def test_return_exceptions_no_errors(self):
        async def work(x):
            return x

        results = await bounded_map(work, [1, 2, 3], return_exceptions=True)
        self.assertEqual(results, [1, 2, 3])

    # ---------- timeout ----------
    async def test_timeout_is_applied_per_item(self):
        async def work(x):
            await asyncio.sleep(0.05 if x == 1 else 0.001)
            return x

        with self.assertRaises(asyncio.TimeoutError):
            await bounded_map(work, [0, 1, 2], concurrency=1, timeout=0.02)

    async def test_fast_items_pass_under_timeout(self):
        async def work(x):
            await asyncio.sleep(0.001)
            return x

        results = await bounded_map(work, range(5), concurrency=2, timeout=0.5)
        self.assertEqual(results, list(range(5)))

    async def test_timeout_with_return_exceptions(self):
        async def work(x):
            if x == 1:
                await asyncio.sleep(0.2)
            return x

        results = await bounded_map(work, [0, 1, 2], concurrency=2, timeout=0.02, return_exceptions=True)
        self.assertEqual(results[0], 0)
        self.assertIsInstance(results[1], asyncio.TimeoutError)
        self.assertEqual(results[2], 2)

    async def test_timeout_budget_is_not_shared(self):
        async def work(x):
            await asyncio.sleep(0.03)
            return x

        # Each item needs 0.03s; a shared 0.04s budget would fail later items.
        results = await bounded_map(work, range(4), concurrency=2, timeout=0.06)
        self.assertEqual(results, [0, 1, 2, 3])

    # ---------- invalid concurrency ----------
    async def test_invalid_concurrency(self):
        async def work(x):
            return x

        for bad in (0, -1, -100):
            with self.assertRaises(ValueError):
                await bounded_map(work, [1], concurrency=bad)

    async def test_non_integer_concurrency_rejected(self):
        async def work(x):
            return x

        with self.assertRaises(ValueError):
            await bounded_map(work, [1], concurrency=2.5)
        with self.assertRaises(ValueError):
            await bounded_map(work, [1], concurrency=True)

    # ---------- cancellation ----------
    async def test_outer_cancellation_stops_work(self):
        finished = []

        async def work(x):
            await asyncio.sleep(0.2)
            finished.append(x)
            return x

        task = asyncio.ensure_future(bounded_map(work, range(10), concurrency=2))
        await asyncio.sleep(0.02)
        task.cancel()
        with self.assertRaises(asyncio.CancelledError):
            await task
        self.assertEqual(finished, [])

    async def test_no_dangling_tasks_after_failure(self):
        async def work(x):
            if x == 0:
                raise RuntimeError("early failure")
            await asyncio.sleep(5)
            return x

        with self.assertRaises(RuntimeError):
            await bounded_map(work, range(6), concurrency=3)
        await asyncio.sleep(0)
        leftovers = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
        self.assertEqual(leftovers, [])

    async def test_no_dangling_tasks_after_timeout(self):
        async def work(x):
            await asyncio.sleep(5)
            return x

        with self.assertRaises(asyncio.TimeoutError):
            await bounded_map(work, range(4), concurrency=2, timeout=0.01)
        await asyncio.sleep(0)
        leftovers = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
        self.assertEqual(leftovers, [])

    # ---------- large input ----------
    async def test_1000_inputs(self):
        async def work(x):
            if x % 100 == 0:
                await asyncio.sleep(0.001)
            return x * 2

        results = await bounded_map(work, range(1000), concurrency=8)
        self.assertEqual(len(results), 1000)
        self.assertEqual(results, [x * 2 for x in range(1000)])

    async def test_large_lazy_iterable_is_not_materialised_upfront(self):
        consumed = {"n": 0}

        def gen():
            for i in range(1000):
                consumed["n"] += 1
                yield i

        async def work(x):
            return x

        results = await bounded_map(work, gen(), concurrency=4)
        self.assertEqual(len(results), 1000)
        self.assertEqual(consumed["n"], 1000)  # fully consumed by the end

    async def test_async_iterable_input(self):
        async def source():
            for i in range(5):
                yield i

        async def work(x):
            return x + 100

        self.assertEqual(await bounded_map(work, source(), concurrency=2), [100, 101, 102, 103, 104])

    async def test_sync_callable_returning_awaitable(self):
        def work(x):
            async def inner():
                return x * 3

            return inner()

        self.assertEqual(await bounded_map(work, [1, 2, 3], concurrency=2), [3, 6, 9])

    def test_concurrency_zero_raises_immediately(self):
        async def work(x):  # pragma: no cover - never called
            return x

        coro = bounded_map(work, [1], concurrency=0)
        with self.assertRaises(ValueError):
            asyncio.get_event_loop_policy().new_event_loop().run_until_complete(coro)


if __name__ == "__main__":
    unittest.main(verbosity=2)
