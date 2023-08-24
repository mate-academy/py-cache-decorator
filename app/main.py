from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results_cache = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()))

        if key in results_cache:
            print("Getting from cache")
            return results_cache[key]
        else:
            result = func(*args, **kwargs)
            results_cache[key] = result
            print("Calculating new result")
            return result

    return wrapper
