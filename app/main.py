import time
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_result = {}

    def add_result(*args, **kwargs) -> Callable:
        if args in cache_result and cache_result[args][0] >= time.time():
            print("Getting from cache")
            return cache_result[args][1]
        else:
            result = func(*args, **kwargs)
            cache_result[args] = (time.time() + 3, result)
            print("Calculating new result")
            return result

    return add_result
