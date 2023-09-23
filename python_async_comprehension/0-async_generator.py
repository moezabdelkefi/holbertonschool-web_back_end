#!/usr/bin/env python3
import asyncio
import random
from typing import Generator

"""
 a coroutine called async_generator that takes no arguments
"""


async def async_generator() -> Generator:
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
