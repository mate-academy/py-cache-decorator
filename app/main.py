from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args, **kwargs) -> Any:
        if args not in cache_dict:
            cache_dict[args] = func(*args)
            print("Calculating new result")
            return cache_dict[args]
        else:
            print("Getting from cache")
            return cache_dict[args]

    return inner
