#!/usr/bin/env python3
"""Defines an asynchronous coroutine"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """performa list of delays n times with maximum delay of max_delay"""
    data = [ wait_random(max_delay) for _ in range(n)]
    data = asyncio.as_completed(data)
    delays = [await temp for temp in data]
    return delays
