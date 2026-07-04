from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        if args in cache_storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_storage[args] = func(*args)

        return cache_storage[args]

    return wrapper
