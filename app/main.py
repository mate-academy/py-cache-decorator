import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    memory = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> int:
        # nonlocal memory
        key = (args, tuple(sorted(kwargs.items())))
        if key not in memory:
            memory[key] = func(*args, **kwargs)
            print("Calculating new result")
            return memory[key]
        print("Getting from cache")
        return memory[key]

    return wrapper
