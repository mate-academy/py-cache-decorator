from typing import Callable, Any


def cache(func: Callable) -> Callable:
    store = {}

    def inner(*args: Any) -> Any:
        if args in store:
            print("Getting from cache")
        else:
            store[args] = func(*args)
            print("Calculating new result")
        return store[args]
    return inner
