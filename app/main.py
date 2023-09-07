from typing import Callable


def cache(func: Callable) -> Callable:
    func_cache = {}

    def wrapper(*args, **kwargs) -> dict:
        key = (args, tuple(kwargs.items()))

        if key in func_cache:
            print("Getting from cache")
            return func_cache[key]

        func_cache[key] = func(*args, **kwargs)
        print("Calculating new result")
        return func_cache[key]

    return wrapper
