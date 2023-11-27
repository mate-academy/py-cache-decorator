from typing import Callable


def cache(func: Callable) -> Callable:
    saved_result = {}

    def inner(*args) -> None:
        if args not in saved_result:
            print("Calculating new result")
            saved_result[args] = func(*args)
        else:
            print("Getting from cache")
        return saved_result[args]

    return inner
