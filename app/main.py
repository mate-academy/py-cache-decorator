from typing import Callable, Any


def cache(func: Callable) -> Any:
    stored_cache = {}

    def wrapper(*args: (int, float, str), **kwargs: (tuple, bool)) -> Any:
        if args not in stored_cache:
            stored_cache[args] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return stored_cache[args]

    return wrapper
