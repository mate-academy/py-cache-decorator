from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_results = {}

    def wrapper(*args) -> Any:
        if args in cache_results:
            print("Getting from cache")
            return cache_results[args]

        print("Calculating new result")
        new_result = func(*args)
        cache_results[args] = new_result
        return new_result
    return wrapper
