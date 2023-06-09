#!/usr/bin/env python3
"""Module Containing a Function that tests basic
Async Syntax"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> int:
    """Waits for a random delay between 0 and max_delay
    and returns it."""

    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)

    return num

