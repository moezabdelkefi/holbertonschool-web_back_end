#!/usr/bin/env python3
import asyncio
import random
from typing import List

"""
"""


async def wait_random(max_delay: int = 10) -> float:
    random_delay = random.uniform(0, float(max_delay))

    # Simulate waiting for the random delay asynchronously
    await asyncio.sleep(random_delay)

    return random_delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
