from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_disc = {}

    def new_dict(*args) -> Any:

        if args in cache_disc:
            print("Getting from cache")
            return cache_disc[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_disc[args] = result
            return result
    return new_dict
