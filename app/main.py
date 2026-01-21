from typing import Callable, TypeVar

ReturnType = TypeVar("ReturnType")


def cache(func: Callable) -> Callable:
    cache_results = {}

    def wrapper(*args, **kwargs) -> ReturnType:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_results:
            print("Getting from cache")
            result = cache_results[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_results[key] = result
        return result
    return wrapper
