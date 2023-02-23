from typing import Any, Callable


def cache(func: Callable) -> Callable:
    previous_results = {}

    def wrapper(*args) -> Any:
        if args in previous_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            previous_results[args] = func(*args)
        return previous_results[args]
    return wrapper
