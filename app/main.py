from typing import Callable, Any


def cache(func: Callable) -> Callable:
    dict_cache = {}

    def inner(*args) -> Any:
        if args not in dict_cache:
            print("Calculating new result")
            dict_cache[args] = func(*args)
        else:
            print("Getting from cache")
        return dict_cache[args]
    return inner
