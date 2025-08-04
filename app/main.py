from typing import Callable


def cache(func: Callable) -> Callable:
    func_cache = {}

    def inner(*args) -> int:
        if args in func_cache:
            print("Getting from cache")
            return func_cache[args]
        else:
            result = func(*args)
            func_cache[args] = result
            print("Calculating new result")
            return result

    return inner
