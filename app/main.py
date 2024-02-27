from typing import Callable, Any


def cache(func: Callable) -> Callable:
    store_result = {}

    def wrapper(*args) -> Any:

        if args in store_result:
            print("Getting from cache")
        else:
            print("Calculating new result")
            store_result[args] = func(*args)

        return store_result[args]

    return wrapper
