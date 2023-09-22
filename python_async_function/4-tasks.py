#!/usr/bin/env python3
from typing import List
import asyncio
import random

""" Takes int arg, waits for random delay """


async def task_wait_random(max_delay: int) -> float:
    await asyncio.sleep(random.uniform(0, float(max_delay)))
    return random.uniform(0, float(max_delay))


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    tasks = [asyncio.create_task(task_wait_random(max_delay))
             for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
