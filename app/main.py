from typing import Callable, Any


def cache(func: Callable) -> Callable:

    cached_args = {}

    def wrapper(*args) -> Any:

        if args not in cached_args:
            print("Calculating new result")
            result = func(*args)
            cached_args[args] = result
            return result
        else:
            print("Getting from cache")
            return cached_args[args]

    return wrapper
