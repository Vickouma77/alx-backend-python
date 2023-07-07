#!/usr/bin/env python3
"""
Complex types - list of floats
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return list of tuples
    """
    return [(i, len(i)) for i in lst]
