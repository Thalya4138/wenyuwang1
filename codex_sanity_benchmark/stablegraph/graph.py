"""Stable topological sorting with concrete cycle reporting.

Public API:
    stable_topological_sort(nodes, edges) -> list
"""

import heapq

from .errors import CycleError

__all__ = ["stable_topological_sort", "CycleError"]

_WHITE, _GRAY, _BLACK = 0, 1, 2


def _materialize(nodes, edges):
    """Validate the inputs and return (ordered_nodes, index, adjacency)."""
    try:
        ordered = list(nodes)
    except TypeError as exc:  # pragma: no cover - defensive
        raise ValueError("nodes must be an iterable") from exc

    index = {}
    for position, node in enumerate(ordered):
        try:
            seen = node in index
        except TypeError as exc:
            raise ValueError(f"node {node!r} is unhashable") from exc
        if seen:
            raise ValueError(f"duplicate node in nodes: {node!r}")
        index[node] = position

    adjacency = {node: [] for node in ordered}
    for edge in edges:
        try:
            u, v = edge
        except (TypeError, ValueError) as exc:
            raise ValueError(f"each edge must be a (u, v) pair, got {edge!r}") from exc
        if u not in index:
            raise ValueError(f"edge references unknown node: {u!r}")
        if v not in index:
            raise ValueError(f"edge references unknown node: {v!r}")
        adjacency[u].append(v)

    # Duplicate edges do not change reachability or in-degree.
    for node, targets in adjacency.items():
        if targets:
            adjacency[node] = list(dict.fromkeys(targets))

    return ordered, index, adjacency


def _find_cycle(ordered, index, adjacency):
    """Return a real closed walk (list) taken from actual edges, or None."""
    color = {node: _WHITE for node in ordered}

    for root in ordered:
        if color[root] != _WHITE:
            continue
        # Explicit DFS: each frame is [node, iterator position, targets].
        path = [root]
        path_index = {root: 0}
        color[root] = _GRAY
        stack = [[root, 0, adjacency[root]]]

        while stack:
            frame = stack[-1]
            node, position, targets = frame
            if position < len(targets):
                frame[1] = position + 1
                nxt = targets[position]
                if color[nxt] == _GRAY:
                    # nxt is on the current path: slice out the real cycle.
                    start = path_index[nxt]
                    return path[start:] + [nxt]
                if color[nxt] == _WHITE:
                    color[nxt] = _GRAY
                    path_index[nxt] = len(path)
                    path.append(nxt)
                    stack.append([nxt, 0, adjacency[nxt]])
            else:
                color[node] = _BLACK
                stack.pop()
                path_index.pop(node, None)
                path.pop()
    return None


def stable_topological_sort(nodes, edges):
    """Topologically sort ``nodes`` under ``edges``, preserving input order.

    Args:
        nodes: Iterable of hashable nodes, in the caller's preferred order.
        edges: Iterable of ``(u, v)`` pairs meaning ``u`` must precede ``v``.

    Returns:
        A new ``list`` with every node exactly once. Among nodes that are
        simultaneously eligible, the one appearing earlier in ``nodes`` is
        always emitted first (Kahn + min-heap on the original position).

    Raises:
        ValueError: ``nodes`` contains a duplicate, or an edge references a
            node that is absent from ``nodes``.
        CycleError: The graph contains a cycle. ``CycleError.cycle`` holds a
            real closed walk of edges, e.g. ``["A", "B", "C", "A"]``.

    Complexity: O(V + E) time (heap operations are O(log V) per node, i.e.
    O(V log V) worst case) and O(V + E) memory. Neither input is mutated.
    """
    ordered, index, adjacency = _materialize(nodes, edges)

    in_degree = {node: 0 for node in ordered}
    for targets in adjacency.values():
        for v in targets:
            in_degree[v] += 1

    # Heap keyed by original position keeps the sort stable and deterministic.
    ready = [index[node] for node in ordered if in_degree[node] == 0]
    heapq.heapify(ready)

    result = []
    while ready:
        position = heapq.heappop(ready)
        node = ordered[position]
        result.append(node)
        for nxt in adjacency[node]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                heapq.heappush(ready, index[nxt])

    if len(result) != len(ordered):
        cycle = _find_cycle(ordered, index, adjacency)
        if cycle is None:  # pragma: no cover - unreachable if logic is sound
            raise ValueError("graph is cyclic but no cycle could be recovered")
        raise CycleError(cycle)

    return result
