from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        value_tuple = args + tuple(kwargs.items())
        if value_tuple not in cache_dict:
            result = func(*args, **kwargs)
            cache_dict[value_tuple] = result
            print("Calculating new result")
            return result
        else:
            print("Getting from cache")
            return cache_dict[value_tuple]
    return wrapper
