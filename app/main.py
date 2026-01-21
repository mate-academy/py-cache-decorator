from typing import Callable, Any


def cache(func: Callable) -> Callable:
    my_store = {}

    def wrapper(*args) -> Any:
        if args in my_store:
            print("Getting from cache")
            return my_store[args]
        print("Calculating new result")
        result = func(*args)
        my_store[args] = result
        return result
    return wrapper
