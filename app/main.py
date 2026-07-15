from typing import Callable


def cache(func: Callable) -> Callable:
    results_cache = {}

    def wrapper(*args, **kwargs) -> func:
        result = (args, tuple(sorted(kwargs.items())))
        if result not in results_cache:
            print("Calculating new result")
            results_cache[result] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return results_cache[result]
    return wrapper
