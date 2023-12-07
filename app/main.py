from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def cache_checker(*args) -> Any:
        if args not in cache_dict.keys():
            print("Calculating new result")
            cache_dict[args] = func(*args)
            return cache_dict[args]
        print("Getting from cache")
        return cache_dict[args]

    return cache_checker
