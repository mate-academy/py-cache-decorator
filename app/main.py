from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dec = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (*args, *kwargs.items())

        if key in cache_dec:
            print("Getting from cache")
            return cache_dec[key]
        else:
            print("Calculating new result")

        result = func(*args, **kwargs)
        cache_dec[key] = result

        return result

    return wrapper
