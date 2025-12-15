from typing import Callable, Any


def cache(func: Callable) -> Callable:
    saved_cache = {}

    def wrapper(*args, **kwargs) -> Any:
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in saved_cache:
            print("Getting from cache")
            return saved_cache[cache_key]

        cache_value = func(*args, **kwargs)
        saved_cache[cache_key] = cache_value
        print("Calculating new result")
        return cache_value

    return wrapper
