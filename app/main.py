from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args) -> Any:
        nonlocal cache_dict
        if args not in cache_dict:
            cache_dict[args] = func(*args)
            print("Calculating new result")
            return cache_dict.get(args)
        else:
            print("Getting from cache")
            return cache_dict.get(args)

    return inner
