from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_results = {}

    def inner(*args) -> Any:
        if args not in stored_results:
            print("Calculating new result")
            stored_results[args] = func(*args)
        else:
            print("Getting from cache")
        return stored_results[args]
    return inner
