#!/usr/bin/env python3
"""Async Comprehension"""

from typing import List, Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[Generator]:
    """coroutine collects 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.

    Returns:
        List[float]: List of 10 random numbers.
    """
    return [i async for i in async_generator()]
