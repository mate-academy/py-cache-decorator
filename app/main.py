from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results_cache = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in results_cache:
            print("Getting from cache")
        else:
            result = func(*args, **kwargs)
            results_cache[key] = result
            print("Calculating new result")
        return results_cache[key]
    return wrapper
