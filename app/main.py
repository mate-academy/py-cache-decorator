from typing import Callable


def cache(func: Callable) -> Callable:
    cache_result = {}

    def wrapper(*args) -> Callable:
        result = (args,)
        if result not in cache_result:
            cache_result[result] = func(*args)
            print("Calculating new result")
            return cache_result[result]
        elif result in cache_result:
            print("Getting from cache")
            return cache_result[result]
    return wrapper
