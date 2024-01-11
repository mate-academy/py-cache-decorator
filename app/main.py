from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    memory = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> dict:
        key = (args, kwargs.items(), func.__name__,)
        if key in memory:
            print("Getting from cache")
        else:
            print("Calculating new result")
            memory[key] = func(*args, **kwargs)
        return memory[key]
    return inner
