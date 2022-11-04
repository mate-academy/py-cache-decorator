from typing import Any, Callable


def cache(func: Callable) -> Any:
    cached_values = {}

    def inner(*args) -> Callable:

        if args in cached_values:
            print("Getting from cache")
            return cached_values[args]

        print("Calculating new result")
        cached_values[args] = func(*args)
        return cached_values[args]

    return inner
