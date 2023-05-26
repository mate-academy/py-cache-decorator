from typing import Callable, Any


def cache(func: Callable) -> Callable:
    arguments = {}

    def inner(*args) -> Any:
        if (*args,) in arguments:
            print("Getting from cache")
            return arguments[*args]
        print("Calculating new result")
        arguments[args] = func(*args)
        return arguments[args]
    return inner
