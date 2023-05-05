#!/usr/bin/env python3

"""Using an async generator in an async list comprehension"""


import asyncio
from typing import List
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Use async comprehension to collect 10
    random numbers by async_generator coroutine"""

    randoms = [n async for n in async_generator()]

    return randoms
