#!/usr/bin/env python3


from typing import List
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time for `wait_n(n, max_delay)`,
    and returns `total_time / n`.
    Returns `float`
    """

    s = time.perf_counter()
    await wait_n(n, max_delay)
    elapsed = time.perf_counter() - s

    return elapsed / n
