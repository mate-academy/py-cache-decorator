from typing import Callable, Any
import functools


def cache(func: Callable) -> Any:
    memory = {}

    @functools.wraps(func)
    def inner(*args) -> Any:
        if args in memory:
            print("Getting from cache")
            return memory.get(args)
        res = func(*args)
        memory[args] = res
        print("Calculating new result")
        return res
    return inner
