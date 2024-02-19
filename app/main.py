from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args, **kwargs):
        cache_key = f"{args=}{kwargs=}"
        nonlocal cached_results
        if cache_key in cached_results:
            print("Getting from cache")
            return cached_results[cache_key]

        result = func(*args, **kwargs)
        cached_results[cache_key] = result
        print("Calculating new result")

        return result
    return wrapper
