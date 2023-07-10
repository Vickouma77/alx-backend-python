#!/usr/bin/env python3
"""
executing multiple coroutines at the same time with async
"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_random(n: int,  max_delay: int = 10) -> float:
    """[summary]

    Args:
        n (int): [description]
        max_delay (int, optional): [description]. Defaults to 10.

    Returns:
        float: [description]
    """
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """[summary]

    Args:
        n (int): [description]
        max_delay (int, optional): [description]. Defaults to 10.

    Returns:
        List[float]: [description]
    """
    tasks = []
    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    return [await task for task in asyncio.as_completed(tasks)]
