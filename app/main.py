from typing import Callable


def cache(func: Callable) -> Callable:
    cached_info = {}

    def inner(*args, **kwargs) -> int:
        sorted_kwargs = tuple(sorted(kwargs.items()))
        set_key = (args, sorted_kwargs)
        if set_key in cached_info:
            print("Getting from cache")
            return cached_info[set_key]
        result = func(*args, **kwargs)
        cached_info[set_key] = result
        print("Calculating new result")
        return result
    return inner
