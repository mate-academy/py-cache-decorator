from typing import Callable, Any


def cache(func: Callable) -> Callable:
    saved_cache = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in saved_cache:
            print("Getting from cache")
            return saved_cache[key]
        else:
            result = func(*args, **kwargs)
            saved_cache[key] = result
            print("Calculating new result")
            return result

    return wrapper
