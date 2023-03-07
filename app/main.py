from typing import Callable


def cache(func: Callable) -> Callable:
    dict_of_cache = {}

    def wrapper(*args) -> dict:

        if args in dict_of_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            dict_of_cache[args] = func(*args)

        return dict_of_cache[args]

    return wrapper
