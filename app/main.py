from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_result = dict()

    def inner(*args) -> Any:
        if args in cache_result:
            print("Getting from cache")
            return cache_result[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_result[args] = result
            return result
    return inner
