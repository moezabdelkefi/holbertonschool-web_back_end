import asyncio
import random
"""
 an asynchronous coroutine that takes in an integer argument
 (max_delay, with a default value of 10) named wait_random that waits
 for a random delay between 0 and max_delay (included and float value)
 seconds and eventually returns it
"""


async def wait_random(max_delay=10):
    random_delay = random.uniform(0, float(max_delay))

    # Simulate waiting for the random delay asynchronously
    await asyncio.sleep(random_delay)

    return random_delay
