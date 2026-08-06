from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cache_collector = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        input_ = (args, tuple(sorted(kwargs.items())))
        if input_ in cache_collector:
            print("Getting from cache")

        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_collector[input_] = result
        return cache_collector[input_]

    return wrapper
