from typing import Callable


def cache(func: Callable) -> Callable:

    completed_calculations = {}

    def wrapper(*args, **kwargs) -> Callable:

        if completed_calculations.get(args, None) is None:
            print("Calculating new result")
            completed_calculations[args] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return completed_calculations[args]

    return wrapper
