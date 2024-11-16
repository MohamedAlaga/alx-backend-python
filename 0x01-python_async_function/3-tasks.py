#!/usr/bin/env python3
"""create tasks"""
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """create task"""
    return asyncio.create_task(wait_random(max_delay))
