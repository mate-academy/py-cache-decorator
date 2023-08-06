from typing import Callable


def cache(func: Callable) -> str:
    cache_result = {}

    def inner(*args, **kwargs) -> Callable:
        if args in cache_result:
            print("Getting from cache")
            return cache_result[args]
        else:
            result = func(*args, **kwargs)
            cache_result[args] = result
            print("Calculating new result")
            return result

    return inner
