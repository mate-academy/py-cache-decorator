from typing import Callable, Any


def cache(func: Callable) -> Callable:
    saved_results = {}

    def inner(*args) -> Any:
        if args in saved_results:
            print("Getting from cache")
            return saved_results[args]

        if args not in saved_results:
            print("Calculating new result")
            result = func(*args)
            saved_results[args] = result
            return result
    return inner
