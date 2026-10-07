"""A tiny dependency-free package for stable topological sorting."""

from .errors import CycleError
from .graph import stable_topological_sort

__all__ = ["stable_topological_sort", "CycleError"]
