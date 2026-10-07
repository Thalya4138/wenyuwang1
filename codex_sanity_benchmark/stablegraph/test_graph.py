"""Tests for stablegraph.stable_topological_sort.

Runs under pytest or, failing that, ``python -m unittest``.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stablegraph import CycleError, stable_topological_sort  # noqa: E402


def assert_valid_topological_order(test, result, nodes, edges):
    """Every node present exactly once, and every edge respected."""
    test.assertEqual(len(result), len(list(nodes)))
    test.assertEqual(set(result), set(nodes))
    position = {node: i for i, node in enumerate(result)}
    for u, v in edges:
        test.assertLess(position[u], position[v], f"edge {u}->{v} violated")


class TestStableTopologicalSort(unittest.TestCase):
    # 1
    def test_empty_graph(self):
        self.assertEqual(stable_topological_sort([], []), [])

    # 2
    def test_single_node(self):
        self.assertEqual(stable_topological_sort(["A"], []), ["A"])

    # 3
    def test_isolated_nodes_keep_order(self):
        nodes = ["A", "B", "C", "D"]
        self.assertEqual(stable_topological_sort(nodes, []), nodes)

    # 4
    def test_simple_chain(self):
        nodes = ["A", "B", "C"]
        edges = [("A", "B"), ("B", "C")]
        self.assertEqual(stable_topological_sort(nodes, edges), ["A", "B", "C"])

    # 4b: chain given in reverse declaration order must still sort correctly
    def test_chain_declared_out_of_order(self):
        nodes = ["C", "B", "A"]
        edges = [("A", "B"), ("B", "C")]
        self.assertEqual(stable_topological_sort(nodes, edges), ["A", "B", "C"])

    # 5
    def test_diamond_graph(self):
        nodes = ["A", "B", "C", "D"]
        edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")]
        result = stable_topological_sort(nodes, edges)
        assert_valid_topological_order(self, result, nodes, edges)
        self.assertEqual(result, ["A", "B", "C", "D"])

    # 6
    def test_stability_with_multiple_choices(self):
        nodes = ["root", "z", "m", "a"]
        edges = [("root", "z"), ("root", "m"), ("root", "a")]
        result = stable_topological_sort(nodes, edges)
        self.assertEqual(result, ["root", "z", "m", "a"])
        assert_valid_topological_order(self, result, nodes, edges)

    def test_stability_after_parallel_branches(self):
        # After "root", all three are free: original order must be preserved,
        # even though alphabetical order would differ.
        nodes = ["root", "c", "a", "b"]
        edges = [("root", "c"), ("root", "a"), ("root", "b")]
        self.assertEqual(stable_topological_sort(nodes, edges), ["root", "c", "a", "b"])

    # 7
    def test_disconnected_graph(self):
        nodes = ["A", "B", "C", "D", "E"]
        edges = [("A", "B"), ("D", "E")]
        result = stable_topological_sort(nodes, edges)
        assert_valid_topological_order(self, result, nodes, edges)
        self.assertEqual(result, ["A", "B", "C", "D", "E"])

    # 8
    def test_duplicate_edges_are_harmless(self):
        nodes = ["A", "B", "C"]
        edges = [("A", "B"), ("A", "B"), ("B", "C"), ("A", "B")]
        self.assertEqual(stable_topological_sort(nodes, edges), ["A", "B", "C"])

    # 9
    def test_unknown_node_in_edge(self):
        with self.assertRaises(ValueError):
            stable_topological_sort(["A", "B"], [("A", "Z")])
        with self.assertRaises(ValueError):
            stable_topological_sort(["A", "B"], [("Z", "A")])

    # 10
    def test_duplicate_node(self):
        with self.assertRaises(ValueError):
            stable_topological_sort(["A", "B", "A"], [])

    # 11
    def test_self_loop(self):
        with self.assertRaises(CycleError) as ctx:
            stable_topological_sort(["A", "B"], [("A", "A")])
        cycle = ctx.exception.cycle
        self.assertEqual(cycle, ["A", "A"])
        self.assertEqual(cycle[0], cycle[-1])

    # 12
    def test_two_node_cycle(self):
        with self.assertRaises(CycleError) as ctx:
            stable_topological_sort(["A", "B"], [("A", "B"), ("B", "A")])
        cycle = ctx.exception.cycle
        self.assertEqual(cycle[0], cycle[-1])
        self.assertEqual(len(cycle), 3)  # A, B, A
        self.assertEqual(set(cycle), {"A", "B"})

    # 13
    def test_three_node_cycle(self):
        nodes = ["A", "B", "C"]
        edges = [("A", "B"), ("B", "C"), ("C", "A")]
        with self.assertRaises(CycleError) as ctx:
            stable_topological_sort(nodes, edges)
        cycle = ctx.exception.cycle
        self.assertEqual(cycle[0], cycle[-1])
        self.assertEqual(sorted(set(cycle)), ["A", "B", "C"])
        self.assertEqual(len(cycle), 4)  # A, B, C, A

    # 14
    def test_cycle_edges_really_exist_in_graph(self):
        nodes = ["A", "B", "C", "D", "E", "F"]
        edges = [
            ("A", "B"),
            ("D", "E"),
            ("E", "F"),
            ("F", "D"),  # the only cycle: D -> E -> F -> D
            ("B", "C"),
        ]
        edge_set = set(edges)
        with self.assertRaises(CycleError) as ctx:
            stable_topological_sort(nodes, edges)
        cycle = ctx.exception.cycle
        self.assertEqual(cycle[0], cycle[-1])
        self.assertGreaterEqual(len(cycle), 2)
        for u, v in zip(cycle, cycle[1:]):
            self.assertIn((u, v), edge_set, f"reported edge {u}->{v} is not in the graph")
        self.assertEqual(set(cycle), {"D", "E", "F"})

    def test_cycle_is_reported_with_extra_context(self):
        # Cycle is not reachable from every node; it still must be found.
        nodes = ["x", "y", "A", "B", "C"]
        edges = [("x", "y"), ("C", "A"), ("A", "B"), ("B", "C")]
        with self.assertRaises(CycleError) as ctx:
            stable_topological_sort(nodes, edges)
        cycle = ctx.exception.cycle
        edge_set = set(edges)
        for u, v in zip(cycle, cycle[1:]):
            self.assertIn((u, v), edge_set)
        self.assertEqual(set(cycle), {"A", "B", "C"})

    def test_cycle_error_is_value_error(self):
        self.assertTrue(issubclass(CycleError, ValueError))

    # 15
    def test_inputs_are_not_modified(self):
        nodes = ["A", "B", "C", "D"]
        edges = [("A", "B"), ("B", "C"), ("C", "D")]
        nodes_copy = list(nodes)
        edges_copy = [tuple(e) for e in edges]
        stable_topological_sort(nodes, edges)
        self.assertEqual(nodes, nodes_copy)
        self.assertEqual(edges, edges_copy)

    def test_accepts_arbitrary_iterables(self):
        nodes = iter(["A", "B", "C"])
        edges = iter([("A", "B")])
        self.assertEqual(stable_topological_sort(nodes, edges), ["A", "B", "C"])

    def test_returns_new_list_not_the_input(self):
        nodes = ["A", "B"]
        result = stable_topological_sort(nodes, [])
        self.assertIsInstance(result, list)
        self.assertIsNot(result, nodes)

    def test_larger_random_dag(self):
        nodes = [f"n{i}" for i in range(200)]
        edges = [(f"n{i}", f"n{j}") for i in range(200) for j in range(i + 1, min(i + 4, 200))]
        result = stable_topological_sort(nodes, edges)
        assert_valid_topological_order(self, result, nodes, edges)
        self.assertEqual(result, nodes)


if __name__ == "__main__":
    unittest.main(verbosity=2)
