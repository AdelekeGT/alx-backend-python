#!/usr/bin/env python3
"""Runtime for four parallel comprehensions"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measures the total runtime and returns it"""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.time()
    return end - start
