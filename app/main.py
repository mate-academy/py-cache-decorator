from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key in cached_results:
            print("Getting from cache")
        else:
            cached_results[key] = func(*args, **kwargs)
            print("Calculating new result")

        return cached_results[key]
    return wrapper
