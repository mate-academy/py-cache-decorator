from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args) -> Callable:
        key = (func.__name__, args)

        if key in cache_dict:
            print("Getting from cache")
            return cache_dict.get(key)

        else:
            print("Calculating new result")
            function_result = func(*args)
            cache_dict.setdefault(key, function_result)
            return function_result

    return wrapper
