#!/usr/bin/env python3
"""
Tasks 5
"""

import asyncio
import random


async def task_wait_n(max_delay: int, n: int) -> float:
    """[summary]

    Args:
        max_delay (int): [description]
        n (int): [description]

    Returns:
        List[float]: [description]
    """
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
