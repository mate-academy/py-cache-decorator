from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    memory = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> dict:
        if args in memory.keys():
            print("Getting from cache")
        else:
            print("Calculating new result")
            memory[args] = func(*args)
        return memory[args]
    return inner
