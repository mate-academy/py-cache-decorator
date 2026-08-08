from typing import Callable


def cache(func: Callable) -> Callable:

    cached_dict = dict()

    def inner(*args, **kwargs) -> Callable:
        if args in cached_dict.keys():
            print("Getting from cache")
            return cached_dict[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_dict[args] = result
            return result
    return inner
