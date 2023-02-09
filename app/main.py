from typing import Any, Callable


def cache(func: Callable) -> Callable:
    previous_results = {}

    def wrapper(*args) -> Any:
        if args in previous_results:
            print("Getting from cache")
            return previous_results[*args]

        print("Calculating new result")
        result = func(*args)
        previous_results[args] = result

        return result

    return wrapper
