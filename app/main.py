from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results_cache = dict()

    def wrapper(*args) -> Any:
        if args in results_cache:
            print("Getting from cache")
            return results_cache[args]
        results_cache[args] = func(*args)
        print("Calculating new result")
        return results_cache[args]

    return wrapper
