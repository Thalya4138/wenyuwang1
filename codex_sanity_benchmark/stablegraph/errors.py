"""Exception types for :mod:`stablegraph`."""


class CycleError(ValueError):
    """Raised when the graph contains a directed cycle.

    The offending cycle is kept on the instance so callers can report a
    concrete loop instead of a bare "cycle exists".

    Attributes:
        cycle: A closed walk of real graph edges, e.g. ``["A", "B", "C", "A"]``.
            Guaranteed to satisfy ``cycle[0] == cycle[-1]`` and to have
            length >= 2 (a self-loop yields ``[u, u]``).
    """

    def __init__(self, cycle):
        self.cycle = list(cycle)
        if not self.cycle or self.cycle[0] != self.cycle[-1]:
            raise ValueError("cycle must be a closed walk: cycle[0] == cycle[-1]")
        super().__init__("cycle detected: " + " -> ".join(str(n) for n in self.cycle))

    def __str__(self):
        return "cycle detected: " + " -> ".join(str(n) for n in self.cycle)

    def __repr__(self):
        return f"CycleError({self.cycle!r})"
