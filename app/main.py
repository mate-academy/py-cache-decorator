from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> int:
        if args not in cache_dict:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[args] = result
        else:
            print("Getting from cache")
            result = cache_dict[args]
        return result
    return wrapper
