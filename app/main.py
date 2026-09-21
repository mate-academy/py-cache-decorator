from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_res = {}

    def wrapper(*args) -> Any:
        if args in cache_res:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_res[args] = func(args)
        return cache_res[args]
    return wrapper
