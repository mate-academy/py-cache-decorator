from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_results = {}

    def inner(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()))
        if key not in stored_results:
            print("Calculating new result")
            stored_results[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return stored_results[key]
    return inner
