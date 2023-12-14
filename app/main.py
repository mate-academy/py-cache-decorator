from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (func, args, frozenset(kwargs.items()))
        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cached_results[key] = result
        return result
    return wrapper
