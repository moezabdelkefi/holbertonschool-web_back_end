#!/usr/bin/env python3

from typing import List
async_generator = __import__('0-async_generator').async_generator

"""
coroutine will collect 10 random numbers using
an async comprehension over async_generator, then return the
10 random numbers.
"""


async def async_comprehension() -> List[float]:
    return [await i async for i in async_generator()]
