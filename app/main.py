from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @wraps(func)
    def inner(*args) -> Any:
        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[args]
        result = func(*args)
        cache_storage[args] = result
        print("Calculating new result")
        return result

    return inner
