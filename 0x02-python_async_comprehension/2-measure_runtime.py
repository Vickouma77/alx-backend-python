#!/usr/bin/env python3
"""
Run time for four parallel comprehensions - async
"""

import asyncio
import random
from typing import Generator, List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime"""
    start = asyncio.get_running_loop().time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = asyncio.get_running_loop().time()
    return end - start
