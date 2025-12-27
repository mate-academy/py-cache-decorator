from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache = {}

    @wraps(func)
    def inner(*args: Any) -> Any:
        if args in cache:
            print("Getting from cache")
        else:
            cache[args] = func(*args)
            print("Calculating new result")
        return cache[args]
    return inner
