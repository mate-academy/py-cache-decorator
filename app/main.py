from typing import Callable, Any


def cache(func: Callable) -> Any:
    cached_args = {}

    def wrapper(*args, **kwargs) -> Any:
        frozen_kwargs = tuple(sorted(kwargs.items()))
        cache_key = (args, frozen_kwargs)
        if cache_key not in cached_args:
            print("Calculating new result")
            cached_args[cache_key] = func(*args, **kwargs)
        print("Getting from cache")
        return cached_args[cache_key]
    return wrapper
