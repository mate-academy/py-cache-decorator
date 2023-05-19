from typing import Callable, Any


def cache(func: Callable) -> Callable:

    cache_dict = {}

    def inner(*args) -> Any:
        nonlocal cache_dict
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]
        print("Calculating new result")
        res = func(*args)
        cache_dict[args] = res
        return res
    return inner
