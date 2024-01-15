#!/usr/bin/env python3
"""module files for task 0"""
import asyncio as asyncf
from random import uniform as uni


async def wait_random(max_delay: int = 10) -> float:
    """async function that waits for a random delay between 0 and max_delay"""
    aDelay = uni(0, max_delay)
    await asyncf.sleep(aDelay)
    return aDelay
