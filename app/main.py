from typing import Callable


def cache(func: Callable) -> Callable:

    execution_cache = {}

    def wrapper(*args, **kwargs) -> any:
        cache_key = args, tuple(kwargs.items())

        if cache_key not in execution_cache:
            execution_cache[cache_key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return execution_cache[cache_key]

    return wrapper
