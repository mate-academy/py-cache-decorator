from typing import Callable, Any


def cache(func: Callable) -> Callable:
    saved_result = {}

    def wrapper(*args, **kwargs) -> Any:
        if args in saved_result:
            print("Getting from cache")
            return saved_result[args]

        print("Calculating new result")
        result = func(*args, **kwargs)
        saved_result[args] = result
        return result
    return wrapper
