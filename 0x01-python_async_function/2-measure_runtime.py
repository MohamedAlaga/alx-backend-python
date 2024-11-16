#!/usr/bin/env python3
"""Defines an asynchronous coroutine"""

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    calc the execution time
    :param n: times of execution
    :param max_delay: maximum time to wait
    :return: average execution time
    """
    return sum(wait_n(n, max_delay)) / n
