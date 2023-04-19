from typing import Callable


def cache(func: Callable) -> Callable:
    local_cache = {}

    def wrapper(*args) -> int:
        if all(isinstance(arg, (int, str, float, tuple)) for arg in args):
            if args in local_cache:
                print("Getting from cache")
                return local_cache[args]
            else:
                value = func(*args)
                local_cache[args] = value
                print("Calculating new result")
                return value
    return wrapper
