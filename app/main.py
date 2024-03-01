from typing import Callable


def cache(func: Callable) -> Callable:
    cache_result = {}

    def wrapper(*args, **kwargs) -> str:
        arguments = args + tuple(kwargs.items())
        if arguments not in cache_result:
            print("Calculating new result")
            cache_result[arguments] = func(*args, **kwargs)
            return cache_result[arguments]
        else:
            print("Getting from cache")
            return cache_result[arguments]

    return wrapper



