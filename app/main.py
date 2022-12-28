from typing import Callable


def cache(func: Callable) -> Callable:
    dict1 = {}

    def wrapper(*args: tuple) -> int:
        if args not in dict1:
            dict1[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return dict1[args]
    return wrapper
