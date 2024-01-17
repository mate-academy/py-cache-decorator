from typing import Callable


def cache(func: Callable) -> Callable:
    res = {}

    def wrapper(*args) -> Callable:
        if args in res:
            print("Getting from cache")
            return res[args]
        else:
            print("Calculating new result")
            res[args] = func(*args)
            return res[args]
    return wrapper
