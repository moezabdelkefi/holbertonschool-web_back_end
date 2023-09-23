#!/usr/bin/env python3
import asyncio
import random
from typing import Generator

"""
 a coroutine called async_generator that takes no arguments
"""


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random float values between 0 and 10.

    Yields:
        float: A random float value between 0 and 10.

    Usage:
        async for value in async_generator():
            print(value)
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
