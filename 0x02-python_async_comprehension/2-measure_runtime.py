#!/usr/bin/env python3
"""module for task 2"""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """measures the total runtime and returns it"""
    start = time.perf_counter()
    corouts = []
    for i in range(4):
        corouts.append(async_comprehension())
    await asyncio.gather(*corouts)
    elapsed = time.perf_counter() - start
    return elapsed
