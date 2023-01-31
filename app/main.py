from typing import Callable


def cache(func: Callable) -> Callable:
    store = {}

    def wrapper(*args, **kwargs) -> None:
        if args not in store:
            print("Calculating new result")
            store[args] = func(*args, *kwargs)
        else:
            print("Getting from cache")
        return store[args]
    return wrapper
