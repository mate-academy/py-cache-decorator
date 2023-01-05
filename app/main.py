from typing import Callable


def cache(func: Callable) -> None:
    store = {}

    def inner(*args) -> str:
        if args in store:
            print("Getting from cache")
            return store[args]
        store[args] = func(*args)
        print("Calculating new result")
        return func(*args)
    return inner
