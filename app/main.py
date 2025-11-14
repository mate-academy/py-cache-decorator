from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    def inner(*args, **kwargs) -> Any:
        if args in cached_results:
            print("Getting from cache")
            return cached_results[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_results[args] = result
            return result

    return inner
