from typing import Callable


def cache(func: Callable) -> Callable:
    store_results = {}

    def inner(*args) -> str:
        if args in store_results.keys():
            print("Getting from cache")
        else:
            store_results[args] = func(*args)
            print("Calculating new result")
        return store_results[args]
    return inner
