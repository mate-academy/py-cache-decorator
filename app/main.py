from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args: Any) -> int:

        if args not in cache_dict:

            cache_dict[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return cache_dict[args]

    return wrapper
