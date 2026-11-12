from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    def inner(*args: Any, **kwargs: Any) -> Callable:
        cache_key = (args, tuple(sorted(kwargs.items())))
        if cache_key not in cached_results:
            print("Calculating new result")
            cached_results[cache_key] = func(*args, **kwargs)
            return cached_results[cache_key]
        else:
            print("Getting from cache")
        return cached_results[cache_key]
    return inner
