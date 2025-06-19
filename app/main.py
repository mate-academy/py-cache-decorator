from typing import Callable


def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args) -> int:
        if cache.__contains__(args):
            print("Getting from cache")
            return cache[args]

        cache[args] = func(*args)
        print("Calculating new result")
        return cache[args]
    return wrapper
