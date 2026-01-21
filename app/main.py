from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args, **kwargs) -> str:
        key = (args, tuple(kwargs.items()))
        if key in results:
            print("Getting from cache")
        else:
            results[key] = func(*args, **kwargs)
            print("Calculating new result")
        return results[key]

    return wrapper
