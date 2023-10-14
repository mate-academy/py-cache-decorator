from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_runs = {}

    def wrapper(*args) -> Any:
        if args not in stored_runs:
            print("Calculating new result")
            stored_runs[args] = func(*args)
        else:
            print("Getting from cache")
        return stored_runs[args]
    return wrapper
