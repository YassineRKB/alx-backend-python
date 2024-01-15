#!/usr/bin/env python3
"""module files for task 1"""
import asyncio
import random
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns the list of all the delays"""
    dlist = []
    for i in range(n):
        dlist.append(asyncio.create_task(wait_random(max_delay)))
    return sorted(await asyncio.gather(*dlist))
