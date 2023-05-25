from typing import Callable, Any


def cache(func: Callable) -> Callable:
    some_dict = {}

    def wrapper(*args) -> Any:
        if args in some_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            some_dict[args] = func(*args)
        return some_dict[args]

    return wrapper
