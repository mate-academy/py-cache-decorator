import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    memory = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()))

        if key in memory:
            print("Getting from cache")
            return memory[key]

        result = func(*args, **kwargs)
        memory[key] = result
        print("Calculating new result")
        return result

    return wrapper
