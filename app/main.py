from typing import Callable, Any


def cache(func: Callable) -> Callable:
    incoming_args = {}

    def inner(*args) -> Any:
        if args not in incoming_args:
            print("Calculating new result")
            incoming_args[args] = func(*args)
        else:
            print("Getting from cache")

        return incoming_args[args]
    return inner
