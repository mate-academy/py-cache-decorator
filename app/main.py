from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    memory = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> dict:
        if args:
            par = args
        else:
            par = tuple(kwargs.values())
        if par in memory:
            print("Getting from cache")
        else:
            print("Calculating new result")
            memory[par] = func(*args, **kwargs)
        return memory[par]
    return inner
