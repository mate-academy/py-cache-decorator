from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_cache = {}

    def wrapper(*args) -> Any:
        if args not in stored_cache:
            stored_cache[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return stored_cache[args]
    return wrapper
