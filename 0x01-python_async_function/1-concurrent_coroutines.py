#!/usr/bin/env python3
"""module files for task 1"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """async function that waits for a random delay between 0 and max_delay"""
    jobs = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(jobs)]
