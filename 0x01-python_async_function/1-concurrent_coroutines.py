#!/usr/bin/env python3
"""Defines an asynchronous coroutine"""
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """performa list of delays n times with maximum delay of max_delay"""
    data = []
    for i in range(n):
        x = await wait_random(max_delay)
        data.append(x)
    return data
