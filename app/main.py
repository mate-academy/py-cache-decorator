from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args, **kwargs) -> Callable:
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in cached_results:
            print("Getting from cache")
            return cached_results[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cached_results[cache_key] = result
        return result

    return wrapper
