from typing import Callable


def cache(func: Callable) -> Callable:
    cache_results = {}

    def wrapper(*args, **kwargs) -> any:
        if args in cache_results:
            print("Getting from cache")
            result = cache_results[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_results[args] = result
        return result

    return wrapper
