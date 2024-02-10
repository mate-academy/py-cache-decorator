from typing import Callable, Any


def cache(func: Callable) -> Callable:
    saved_results = {}

    def wrapper(*args) -> Any:
        key = args
        if key in saved_results:
            print("Getting from cache")
            return saved_results[key]
        else:
            print("Calculating new result")
            result = func(*args)
            saved_results[key] = result
            return result
    return wrapper
