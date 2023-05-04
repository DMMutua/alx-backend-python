#!/usr/bin/env python3
"""A Module Presenting a Function that
runs concurrent coroutines"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """ spawn `wait_random` `n` times with the specified `max_delay`.
    Return the list of all the delays (float values).
    list of the delays should be in ascending order without using
    sort() because of concurrency.
    """

    tasks = []
    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
