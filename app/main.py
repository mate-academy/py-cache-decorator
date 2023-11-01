from typing import Callable


def cache(func: Callable) -> Callable:
    cached_result = {}

    def wrapper(*args, **kwargs) -> None:
        key = (args, frozenset(kwargs))
        if key in cached_result:
            print("Getting from cache")
            return cached_result[key]
        else:
            result = func(*args, **kwargs)
            print("Calculating new result")
            cached_result[key] = result
            return result
    return wrapper
