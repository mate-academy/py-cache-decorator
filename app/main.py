from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    def inner(*args, **kwargs) -> Any:
        if args in cached_results.keys():
            print("Getting from cache")
            solution = cached_results[args]
        else:
            print("Calculating new result")
            solution = func(*args, **kwargs)
            cached_results[args] = solution
        return solution

    return inner
