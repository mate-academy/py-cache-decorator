from typing import Callable


def cache(func: Callable) -> Callable:
    store = {}

    def inner(*args) -> (int, float):
        key = args
        if key in store:
            print("Getting from cache")
            return store[key]
        print("Calculating new result")
        result = func(*args)
        store[key] = result
        return result
    return inner
