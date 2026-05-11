from typing import Callable, Any


def cache(func: Callable) -> Callable:
    store = {}

    def wrapper(*args) -> Any:
        if args in store:
            print("Getting from cache")
            return store[args]

        print("Calculating new result")
        result = func(*args)
        store[args] = result
        return result

    return wrapper
