from typing import Callable, Any


def cache(func: Callable) -> Callable:
    dict_of_cache = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, tuple(kwargs.items()))

        if key in dict_of_cache:
            print("Getting from cache")
            result = dict_of_cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            dict_of_cache[key] = result

        return result

    return wrapper
