from typing import Callable, Union


def cache(func: Callable) -> Callable:
    history = {}

    def inner(*args: tuple) -> None:
        # (mx: The use of `|` for type annotations, was added in Python 3.10)
        if args in history:
            print("Getting from cache")
            return history[args]
        print("Calculating new result")
        result = func(*args)
        history[args] = result
        return result
    return inner
