from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_cache = {}

    def wrapper(*args) -> Any:
        if args not in stored_cache:
            result = func(*args)
            stored_cache[args] = result
            print("Calculating new result")
            return result
        if args in stored_cache:
            print("Getting from cache")
            return stored_cache[args]
    return wrapper
