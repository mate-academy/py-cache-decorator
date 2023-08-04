from typing import Callable, Any


def cache(func: Callable) -> Callable:

    cache_with_results = {}

    def wrapper(*args: Any) -> Any:
        if args in cache_with_results:
            print("Getting from cache")
            return cache_with_results[args]

        cache_with_results[args] = func(*args)
        print("Calculating new result")
        return cache_with_results[args]

    return wrapper
