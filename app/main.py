from typing import Callable


def cache(func: Callable) -> Callable:
    func_cache = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = args
        if key in func_cache:
            print("Getting from cache")
            return func_cache[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        func_cache[key] = result
        return result

    return wrapper
