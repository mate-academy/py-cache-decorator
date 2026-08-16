from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_results = {}

    def wrapper(*args, **kwargs) -> Any:
        current_args = (args)
        if current_args not in stored_results:
            print("Calculating new result")
            stored_results[current_args] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return stored_results[current_args]

    return wrapper
