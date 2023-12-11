from typing import Callable


def cache(func: Callable) -> Callable:

    result_history = {}

    def wrapper(*args) -> Callable:

        if args not in result_history:
            result_history[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return result_history[args]
    return wrapper
