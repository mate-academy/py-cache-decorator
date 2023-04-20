from typing import Callable


def cache(func: Callable) -> Callable:
    local_cache = {}

    def wrapper(*args) -> int:
        if args in local_cache:
            print("Getting from cache")
        else:
            local_cache[args] = func(*args)
            print("Calculating new result")
        return local_cache[args]
    return wrapper
