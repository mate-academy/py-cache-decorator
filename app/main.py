from typing import Callable, Any


def cache(func: Callable) -> Callable:
    saved_results = {}

    def inner(*args) -> Any:
        if args not in saved_results:
            print("Calculating new result")
            saved_results[args] = func(*args)
        else:
            print("Getting from cache")
        return saved_results[args]
    return inner
