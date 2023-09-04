import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    memory = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()))

        if key in memory:
            print("Getting from cache")
        else:
            memory[key] = func(*args, **kwargs)
            print("Calculating new result")
        return memory[key]

    return wrapper
