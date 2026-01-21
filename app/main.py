from typing import Callable, Any


def cache(func: Callable) -> Callable:
    saved_results = {}

    def wrapper(*args: Any) -> Any:
        if args in saved_results:
            print("Getting from cache")
            return saved_results[args]

        result = func(*args)
        print("Calculating new result")
        saved_results[args] = result
        return result

    return wrapper
