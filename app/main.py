from typing import Callable


def cache(func: Callable) -> Callable:
    stored_results = {}
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))

        if key in stored_results:
            print("Getting from cache")
            return stored_results[key]
        else:
            result = func(*args, **kwargs)
            stored_results[key] = result
            print("Calculating new result")
            return result
    return wrapper
