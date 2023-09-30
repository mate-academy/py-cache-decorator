from typing import Callable


def cache(func: Callable) -> Callable:
    cached_result = {}

    def inner(*args, **kwargs) -> Callable:
        if args in cached_result:
            print("Getting from cache")
            return cached_result[args]
        cached_result[args] = func(*args, **kwargs)
        print("Calculating new result")
        return cached_result[args]
    return inner
