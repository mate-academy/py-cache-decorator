from typing import Callable, Any


def cache(func: Callable) -> Callable:
    saved_results = {}

    def wrapper(*args) -> Any:
        key = args
        if key in saved_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            saved_results[key] = func(*args)
        return saved_results[key]
    return wrapper
