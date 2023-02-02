from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    def inner(*args, **kwargs) -> Any:
        if func in cached_results and args in cached_results[func].keys():
            print("Getting from cache")
            return cached_results[func][args]
        solution = func(*args, **kwargs)
        if func in cached_results:
            cached_results[func][args] = solution
        else:
            cached_results[func] = {args: solution}
        print("Calculating new result")
        return solution

    return inner
