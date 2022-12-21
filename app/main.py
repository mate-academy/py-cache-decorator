from typing import Any
from typing import Callable


def cache(func: Callable) -> Callable:
    results_in_cache = {}

    def inner(*args) -> Any:
        if args not in results_in_cache:
            print("Calculating new result")
            results_in_cache[tuple(args)] = func(*args)
        else:
            print("Getting from cache")
        return results_in_cache[tuple(args)]

    return inner
