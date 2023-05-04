#!/usr/bin/env python3

"""A module further demonstrating asyncio Tasks"""

import asyncio
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """ spawn `wait_random` `n` times with the specified `max_delay`.
    Return the list of all the delays (float values).
    list of the delays should be in ascending order without using
    sort() because of concurrency.
    """

    tasks = []
    for i in range(n):
        tasks.append(task_wait_random(max_delay))

    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
