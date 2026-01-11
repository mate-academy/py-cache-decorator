from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args) -> int:
        if args in cache_dict:
            print("Getting from cache ")
            return cache_dict[args]
        else:
            print("Calculating new result")
            function_result = func(*args)
            cache_dict[args] = function_result
            return function_result
    return inner
