from typing import Callable


def cache(func: Callable) -> None:
    store = {}

    def inner(*args) -> str:
        if args in store:
            print("Getting from cache")
            return store[args]
        else:
            result = func(*args)
            print("Calculating new result")
            store[args] = result
        return result
    return inner
