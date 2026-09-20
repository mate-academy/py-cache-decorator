from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cache_result = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_result:
            print("Getting from cache")
            return cache_result[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_result[key] = result
        return result
    return wrapper
