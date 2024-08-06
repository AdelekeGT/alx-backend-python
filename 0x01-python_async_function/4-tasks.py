#!/usr/bin/env python3
"""Return an asyncio.Task"""

import asyncio
from typing import List
task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function takes in 2 int arguments (in this order): n and max_delay.
    It spawns wait_random n times with the specified max_delay.

    Args:
        n (int): number of times wait_random will be spawned
        max_delay (int): specified delay

    Returns:
        List of delays (float): Should be in ascending order
        without using sort()
    """

    # delays = [await wait_random(max_delay) for _ in range(n)]
    # return sorted(delays)

    tasks = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    return [await task for task in asyncio.as_completed(tasks)]
