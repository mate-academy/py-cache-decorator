from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (func.__name__, args, tuple(sorted(kwargs.items())))
        if key not in results:
            print("Calculating new result")
            results[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return results[key]
    return wrapper
