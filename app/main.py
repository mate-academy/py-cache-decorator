from typing import Callable


def cache(func: Callable) -> Callable:
    cached_result = {}

    def wrapper(*args, **kwargs) -> tuple:
        cached_keys = (args, tuple(kwargs.items()))

        if cached_keys in cached_result:
            print("Getting from cache")
            return cached_result[cached_keys]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cached_result[cached_keys] = result
        return result
    return wrapper
