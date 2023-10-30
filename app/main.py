from typing import Callable


def cache(func: Callable) -> Callable:

    used_arguments = {}

    def wrapper(*args) -> Callable:
        if args not in used_arguments.keys():
            print("Calculating new result")
            result = func(*args)
            used_arguments[args] = result
        else:
            print("Getting from cache")
            result = used_arguments[args]

        return result

    return wrapper
