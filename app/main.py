from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_result = {}

    def cache_wrapper(*args) -> Any:
        if args in cached_result:
            print("Getting from cache")
            return cached_result[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cached_result[args] = result
            return result
    return cache_wrapper
