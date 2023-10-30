from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def decorator(*args, **kwargs) -> Callable:
        key = (args, frozenset(kwargs.items()))

        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]
        else:
            result = func(*args, **kwargs)
            cached_results[key] = result
            print("Calculating new result")
            return result

    return decorator
