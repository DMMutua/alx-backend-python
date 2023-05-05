#!/usr/bin/env python3

"""A Module to Measure Run-time"""


import asyncio
from time import perf_counter
from typing import List
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Executes a Coroutine four times
    and Measures Run-time"""

    start_time = perf_counter()

    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    end_time = perf_counter()
    runtime = end_time - start_time

    return runtime

