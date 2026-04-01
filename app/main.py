from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_values = {}

    def wrapper(*args, **kwargs) -> Any:
        kwargs_key = tuple(sorted(kwargs.items()))
        full_key = (args, kwargs_key)

        if full_key not in cache_values:
            cache_values[full_key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return cache_values[full_key]

    return wrapper
