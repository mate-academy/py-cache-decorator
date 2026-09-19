from typing import Callable, Any


def cache(func: Callable) -> Callable:
    saved_result = {}

    def wrapper(*args, **kwargs) -> Any:
        key = args
        if key in saved_result:
            print("Getting from cache")
            return saved_result[args]

        print("Calculating new result")
        result = func(*args, **kwargs)
        saved_result[key] = result
        return result
    return wrapper
