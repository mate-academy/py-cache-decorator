from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (func.__name__, args, tuple(sorted(kwargs.items())))
        if key in results:
            print("Getting from cache")
            return results[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            results[key] = result
            return result
    return wrapper
