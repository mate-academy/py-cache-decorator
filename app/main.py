from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    def inner(*args: Any, **kwargs: Any) -> Callable:
        if args not in cached_results:
            print("Calculating new result")
            cached_results[args] = func(*args, **kwargs)
            return cached_results[args]
        else:
            print("Getting from cache")
        return cached_results[args]
    return inner
