from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args, **kwargs) -> int:
        if args in cache_dict.keys():
            result = cache_dict[args]
            print("Getting from cache")
        else:
            result = (func(*args, **kwargs))
            print("Calculating new result")
        cache_dict[args] = result
        return result
    return inner
