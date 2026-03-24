from typing import Callable


def cache(func: Callable) -> Callable:
    result_cache = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in result_cache:
            result = func(*args, **kwargs)
            result_cache[key] = result
            print("Calculating new result")
            return result
        else:
            print("Getting from cache")
            return result_cache[key]
    return wrapper
