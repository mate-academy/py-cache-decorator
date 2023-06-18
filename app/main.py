from typing import Callable, Any


def cache(func: Callable) -> Callable:
    new_cache = {}

    def wrapper(*args) -> Any:
        if args in new_cache:
            print("Getting from cache")
            return new_cache[args]
        new_cache[args] = func(*args)
        print("Calculating new result")
        return new_cache[args]
    return wrapper
