#!/usr/bin/env python3
"""Complex types - string and int/float to tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return tuple of string and float
    Args:
        k: string
        v: int or float
    Returns:
        tuple of string and float
    """
    return (k, v * v)
