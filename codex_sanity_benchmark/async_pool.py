"""Bounded-concurrency async mapping that preserves input order.

Public API:
    bounded_map(func, items, *, concurrency=5, timeout=None, return_exceptions=False)
"""

import asyncio

__all__ = ["bounded_map"]


async def bounded_map(func, items, *, concurrency=5, timeout=None, return_exceptions=False):
    """Apply ``func`` to ``items`` with at most ``concurrency`` calls in flight.

    A fixed pool of worker tasks pulls items from a single async iterator, so
    ``items`` is never fully materialised: memory stays O(concurrency +
    len(items)) for the results list only, and at most ``concurrency`` tasks
    exist at any moment regardless of how long the input is.

    Args:
        func: An async callable (a sync callable returning an awaitable works
            too, since the result is awaited with :func:`asyncio.ensure_future`).
        items: Any synchronous iterable or async iterable.
        concurrency: Maximum number of simultaneous in-flight calls.
        timeout: Per-item timeout in seconds (each item gets its own budget).
        return_exceptions: If True, failures are stored in the result list at
            their item's position and other items keep running. If False, the
            first failure cancels the remaining work and is re-raised.

    Returns:
        A list of results in the same order as ``items``.

    Raises:
        ValueError: ``concurrency`` is not a positive integer.
    """
    if isinstance(concurrency, bool) or not isinstance(concurrency, int):
        raise ValueError(f"concurrency must be a positive integer, got {concurrency!r}")
    if concurrency <= 0:
        raise ValueError(f"concurrency must be positive, got {concurrency!r}")

    if hasattr(items, "__aiter__"):
        iterator = items.__aiter__()
    else:
        iterator = _sync_to_async_iter(items)

    pull_lock = asyncio.Lock()
    results = []

    async def next_indexed():
        """Claim the next (index, item) pair; serialised by a lock."""
        async with pull_lock:
            try:
                item = await iterator.__anext__()
            except StopAsyncIteration:
                return None
            index = len(results)
            results.append(None)  # reserve this slot so ordering is stable
            return index, item

    async def run_one(index, item):
        call = func(item)
        if timeout is None:
            results[index] = await call
        else:
            results[index] = await asyncio.wait_for(call, timeout)
        return index, item

    async def worker():
        while True:
            claimed = await next_indexed()
            if claimed is None:
                return
            index, item = claimed
            try:
                await run_one(index, item)
            except asyncio.CancelledError:
                raise
            except BaseException as exc:  # noqa: BLE001 - deliberately broad
                if not return_exceptions:
                    raise
                results[index] = exc

    workers = [asyncio.ensure_future(worker()) for _ in range(concurrency)]
    try:
        await asyncio.gather(*workers)
    except BaseException as exc:  # noqa: BLE001 - cleanup must cover cancellation
        # A failure with return_exceptions=False, or cancellation of this
        # coroutine: stop the remaining work promptly and don't leave any
        # worker task dangling.
        for task in workers:
            task.cancel()
        await asyncio.gather(*workers, return_exceptions=True)
        if isinstance(exc, asyncio.CancelledError) or not return_exceptions:
            raise
        # Otherwise the failure was already recorded at its own index.
    return results


async def _sync_to_async_iter(items):
    """Adapt a plain iterable so it can be consumed by ``async for``."""
    for item in items:
        yield item
