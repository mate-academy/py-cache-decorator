from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results_in_cache = {}

    def inner(*args) -> Any:
        if args not in results_in_cache:
            print("Calculating new result")
            result_of_func = func(*args)
            results_in_cache[args] = result_of_func
        else:
            print("Getting from cache")
        return results_in_cache[args]

    return inner
