from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cache_memory = {}

    @functools.wraps(func)
    def inner(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_memory:
            result = cache_memory[key]
            print("Getting from cache")
        else:
            result = func(*args, **kwargs)
            cache_memory[key] = result
            print("Calculating new result")
        return result
    return inner
