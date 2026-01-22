from typing import Callable


def cache(func: Callable) -> Callable:
    results_cache = {}

    def wrapper(*args, **kwargs) -> None:
        key = (args, frozenset(kwargs.items()))

        if key in results_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            results_cache[key] = result

        return results_cache[key]
    return wrapper
