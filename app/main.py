from typing import Callable, Any


def cache(func: Callable) -> Any:
    stored_cache = {}

    def wrapper(*args: (int, float, str), **kwargs: (tuple, bool)) -> Any:
        if args not in stored_cache:
            result = func(*args, **kwargs)
            stored_cache[args] = result
            print("Calculating new result")
            return result
        else:
            print("Getting from cache")
            return stored_cache[args]

    return wrapper
