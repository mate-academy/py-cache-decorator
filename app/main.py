from typing import Callable


def cache(func: Callable) -> Callable:
    history = {}

    def inner(*args: tuple) -> None:
        if args in history:
            print("Getting from cache")
            return history[args]
        print("Calculating new result")
        result = func(*args)
        history[args] = result
        return result
    return inner
