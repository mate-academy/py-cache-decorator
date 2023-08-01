from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_arguments = {}

    def inner(*args) -> Any:
        if args in cache_arguments.keys():
            print("Getting from cache")
        else:
            cache_arguments[args] = func(*args)
            print("Calculating new result")
        return cache_arguments[args]

    return inner
