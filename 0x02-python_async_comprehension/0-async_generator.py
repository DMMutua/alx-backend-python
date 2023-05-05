#!/usr/bin/env python3

"""A Module with An Async Generator Function."""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """A Coroutine to Loop 10 times, with 1 second delay
    that Yields a random number in range of 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
