#!/usr/bin/env python3
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random

"""
a function task_wait_random
that takes an integer max_delay and returns
a asyncio.Task.
"""


def task_wait_random(max_delay: int) -> asyncio.Task:
    task = wait_random(max_delay)
    result = asyncio.ensure_future(task)
    return result
