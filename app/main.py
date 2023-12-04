from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results_cache = {}

    def wrapper(*args) -> Any:
        if args not in results_cache:
            print("Calculating new result")
            results_cache[args] = func(*args)
        else:
            print("Getting from cache")
        return results_cache[args]
    return wrapper
