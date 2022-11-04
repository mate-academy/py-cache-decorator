from typing import Callable


def cache(func: Callable) -> Callable:
    """
    A decorator that stores results of completed runs of decorated function
    with different arguments.
    If decorated function runs with repeating arguments it returns stored
    result instead of calling function again.
    """
    archive = {}

    def wrapper(*args: tuple) -> Callable:
        if args in archive:
            print("Getting from cache")
            return archive[args]
        result = func(*args)
        archive[args] = result
        print("Calculating new result")
        return result
    return wrapper
