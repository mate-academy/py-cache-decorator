from typing import Callable, Any


def cache(func: Callable) -> Callable:
    params = {}

    def inner(*args) -> Any:
        if args in params:
            print("Getting from cache")
        else:
            print("Calculating new result")
            params[args] = func(*args)
        return params[args]
    return inner
