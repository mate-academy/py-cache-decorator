from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_results = {}

    def wrapper(*args) -> Any:
        if args in stored_results:
            print("Getting from cache")
        else:
            stored_results[args] = func(*args)
            print("Calculating new result")
        return stored_results[args]
    return wrapper
