from typing import Callable


def cache(func: Callable) -> Callable:
    stored = {}

    def wrapper(*args):
        if args in stored:
            print("Getting from cache")
            return stored[args]
        else:
            print("Calculating new result")
            result = func(*args)
            stored[args] = result
            return result

    return wrapper
