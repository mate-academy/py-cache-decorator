import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_results = {}

    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        if args not in cache_results:
            cache_results[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_results[args]

    return wrapper
