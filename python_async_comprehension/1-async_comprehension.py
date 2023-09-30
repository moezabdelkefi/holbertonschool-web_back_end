#!/usr/bin/env python3
"""
coroutine will collect 10 random numbers using
an async comprehension over async_generator, then return the
10 random numbers.
"""

from typing import List
import random


async def async_generator() -> List[float]:
    """Async Generator that yields random floats"""
    for _ in range(10):
        yield random.uniform(0, 1)


async def async_comprehension() -> List[float]:
    """Async Comprehensions"""
    return [num async for num in async_generator()]
