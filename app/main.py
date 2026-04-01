from typing import Callable
from typing import Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_memory = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:

        key = args + tuple(sorted(kwargs.items()))

        if key in cache_memory:
            print("Getting from cache")
            return cache_memory[key]

        result = func(*args, **kwargs)
        cache_memory[key] = result
        print("Calculating new result")
        return result
    return inner
