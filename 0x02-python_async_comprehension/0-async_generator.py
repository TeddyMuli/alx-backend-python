#!/usr/bin/env python3
"""
Coroutine that loops 10 times, each time asynchronously waits 1 second,
then yields a random number between 0 and 10.
"""
import random
import asyncio


from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that loops 10 times, each time asynchronously waits 1 second,
    then yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
