from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_data = {}

    def wrapper(*args, **kwargs) -> Any:
        cache_key = (args, *kwargs, *kwargs.values())

        if cache_key not in cached_data:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_data[cache_key] = result

            return result
        else:
            print("Getting from cache")
            return cached_data[cache_key]

    return wrapper
