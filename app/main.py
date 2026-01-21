from typing import Callable


def cache(func: Callable) -> Callable:
    func_cache = {}

    def inner(*args) -> Callable:
        if args in func_cache:
            print("Getting from cache")
        else:
            func_cache[args] = func(*args)
            print("Calculating new result")
        return func_cache[args]
    return inner
