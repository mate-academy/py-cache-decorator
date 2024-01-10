from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results_cache = {}

    def inner(*args) -> Any:
        key = args
        if key in results_cache:
            print("Getting from cache")
            return results_cache[key]
        else:
            result = func(*args)
            results_cache[key] = result
            print("Calculating new result")
            return result

    return inner
