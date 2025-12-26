from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_result = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_result:
            print("Getting from cache")
        else:
            cache_result[key] = func(*args, **kwargs)
            print("Calculating new result")
        return cache_result[key]
    return wrapper
