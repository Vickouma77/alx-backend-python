#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return function that multiplies float by multiplier
    Args:
        multiplier: float to multiply by
    Returns:
        function that multiplies float by multiplier
    """

    def multiply(n: float) -> float:
        """
        Return product of n and multiplier
        """
        return n * multiplier
    return multiply
