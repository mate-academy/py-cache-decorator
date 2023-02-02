from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    def inner(*args, **kwargs) -> Any:
        if args in cached_results.keys():
            print("Getting from cache")
            return cached_results[args]
        solution = func(*args, **kwargs)
        cached_results[args] = solution
        print("Calculating new result")
        return solution

    return inner
