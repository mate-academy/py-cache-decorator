from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_result = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        cache_key = (args, tuple(sorted(kwargs.items())))
        if cache_key not in cached_result:
            print("Calculating new result")
            cached_result[cache_key] = func(*args, **kwargs)
            return cached_result[cache_key]
        else:
            print("Getting from cache")
            return cached_result[cache_key]
    return wrapper
