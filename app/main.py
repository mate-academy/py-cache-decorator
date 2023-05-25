from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args) -> Any:
        nonlocal cache_dict
        res = 0
        if args not in cache_dict:
            print("Calculating new result")
            res = func(*args)
            cache_dict[args] = res
        elif args in cache_dict:
            print("Getting from cache")
            res = cache_dict[args]
        return res

    return inner
