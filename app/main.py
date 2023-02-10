from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args) -> Any:
        if args not in cache_dict.keys():
            result = func(*args)
            cache_dict[args] = result
            print("Calculating new result")
            return result

        print("Getting from cache")
        return cache_dict[args]

    return wrapper
