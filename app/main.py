from typing import Callable, Any


def cache(func: Callable) -> Callable:
    saved_results = {}

    def wrapper(*args) -> Any:
        if args in saved_results:
            print("Getting from cache")
            return saved_results[args]
        else:
            print("Calculating new result")
            result = func(*args)
            saved_results[args] = result
            return result

    return wrapper
