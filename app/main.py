import time
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_result = {}

    def inner(*args, **kwargs) -> Any:
        if args in cache_result and cache_result[args][0]:
            print("Getting from cache")
            result = cache_result[args][1]
        else:
            result = func(*args, **kwargs)
            cache_result[args] = (time.time() + 3, result)
            print("Calculating new result")

        return result

    return inner
