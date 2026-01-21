from functools import wraps
from typing import Callable, Any


cache_storage = {}


def cache(func: Callable) -> Callable:
    cache_storage[func] = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args in cache_storage[func]:
            print("Getting from cache")
            return cache_storage[func][args]

        print("Calculating new result")
        result = func(*args)
        cache_storage[func][args] = result
        return result

    return wrapper
