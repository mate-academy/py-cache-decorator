from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_results = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in stored_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            stored_results[key] = func(*args, **kwargs)
        return stored_results[key]
    return wrapper
