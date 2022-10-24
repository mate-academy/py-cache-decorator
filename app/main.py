from typing import Callable


def cache(func: Callable) -> Callable:
    cached_dict = {}

    def wrapper(*args) -> Callable:
        if args in cached_dict.keys():
            print("Getting from cache")
        elif args not in cached_dict.keys():
            cached_dict[args] = func(*args)
            print("Calculating new result")
        return cached_dict[args]
    return wrapper
