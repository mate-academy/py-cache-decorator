from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args, **kwargs) -> Any:
        cache_key = (args, frozenset(kwargs.items()))
        if cache_key in cached_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached_results[cache_key] = func(*args, **kwargs)
        return cached_results[cache_key]
    return wrapper
