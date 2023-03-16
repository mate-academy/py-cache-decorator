from typing import Callable, Any


def cache(func: Callable) -> Any:
    cashed_functions = {}

    def inner(*args) -> Any:
        if args not in cashed_functions.keys():
            print("Calculating new result")
            cashed_functions[args] = func(*args)
        else:
            print("Getting from cache")
        return cashed_functions[args]
    return inner
