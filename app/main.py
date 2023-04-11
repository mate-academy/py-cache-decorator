from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_args = {}

    def wrapper(*args, **kwargs) -> Any:
        key = args
        if key in cache_args:
            print("Getting from cache")
            return cache_args[key]
        cache_args[key] = func(*args, **kwargs)
        print("Calculating new result")
        return cache_args[key]
    return wrapper
