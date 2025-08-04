from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    memory = dict()

    @functools.wraps(func)
    def wrapper(*args) -> Callable:
        if args in memory:
            print("Getting from cache")
            return memory[args]
        else:
            print("Calculating new result")
            result = func(*args)
            memory[args] = result
            return result
    return wrapper
