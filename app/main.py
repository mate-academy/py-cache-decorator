from typing import Any, Callable


def cache(func: Callable) -> Callable:
    stored_results = {}

    def wrapper(*args: Any) -> Any:
        if args in stored_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            stored_results[args] = func(*args)

        return stored_results[args]

    return wrapper
