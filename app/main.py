from typing import Callable


def cache(func: Callable) -> int:
    cache_dict = {}

    def wrapper(*args) -> int:
        if str(args) not in cache_dict.keys():
            print("Calculating new result")
            result = func(*args)
            cache_dict[str(args)] = result
            return cache_dict[str(args)]
        else:
            print("Getting from cache")
            return cache_dict[str(args)]
    return wrapper
