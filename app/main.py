from typing import Callable, Any


def cache(func: Callable) -> Callable:
    previous_args = {}

    def inner(*args) -> Any:
        if all([
            isinstance(arg, (tuple, str, int, float, bool))
            for arg in args
        ]):
            if args in previous_args:
                print("Getting from cache")
            else:
                previous_args[args] = func(*args)
                print("Calculating new result")
            return previous_args[args]

    return inner
