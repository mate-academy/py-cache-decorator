from typing import Callable, Any

from functools import wraps

cache_results = {}


def cache(func: Callable) -> Callable:
    cache_results = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_results[key] = func(*args, **kwargs)

        return cache_results[key]

    return inner
