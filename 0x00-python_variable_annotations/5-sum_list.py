#!/usr/bin/env python3
"""Complex types - list of floats"""
from typing import List


def sum_list(input_list: float) -> float:
    """Return sum of list of floats
    Args:
        input_list: list of floats
    Returns:
        sum of input_list
    """
    return float(sum(input_list))
