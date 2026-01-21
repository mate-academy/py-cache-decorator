from typing import Callable


def cache(func: Callable) -> Callable:
    cashes = {}

    def wrapper(*args) -> Callable:
        if (args, func.__name__) not in cashes:
            print("Calculating new result")
            res = func(*args)
            cashes[args, func.__name__] = res
            return res
        print("Getting from cache")
        return cashes[args, func.__name__]

    return wrapper
