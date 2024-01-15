#!/usr/bin/env python3
"""module files for task 0"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """async function that waits for a random delay between 0 and max_delay"""
    aDelay: float = random.uniform(0, max_delay)
    await asyncio.sleep(aDelay)
    return aDelay
