from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args, **kwargs) -> int:
        cache_record_key = (args, tuple(frozenset(kwargs.items())))
        if cache_dict:
            if cache_record_key in cache_dict:
                print("Getting from cache")
                return cache_dict[cache_record_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[cache_record_key] = result
        return result
    return inner
