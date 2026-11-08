from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    memory = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> None:

        key = (args, tuple(sorted(kwargs.items())))

        if key in memory:
            print("Getting from cache")
            return memory[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        memory[key] = result
        return result

    return wrapper
