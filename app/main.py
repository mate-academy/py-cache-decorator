from typing import Callable


def cache(func: Callable) -> Callable:
    list_of_old_cache = {}

    def inner(*args: list) -> list:
        if args not in list_of_old_cache:
            list_of_old_cache[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return func(*args)
    return inner
