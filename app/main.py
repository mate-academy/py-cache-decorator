from functools import wraps
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cache = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if (args) in cache.keys():
            print("Getting from cache")
            return cache.get((args))
        else:
            result = func(*args)
            cache[args] = result
            print("Calculating new result")
            return result
    return wrapper
