from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_info = {}

    def inner(*args, **kwargs) -> Any:
        cache_key = (args, frozenset(kwargs.items()))

        if cache_key in cached_info:
            print("Getting from cache")
            return cached_info[cache_key]

        result_of_function = func(*args, **kwargs)
        cached_info[cache_key] = result_of_function
        print("Calculating new result")
        return result_of_function
    return inner
