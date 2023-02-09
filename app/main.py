from typing import Callable, Any


def cache(func: Callable) -> Callable:
    array = {}

    def wrapper(*args) -> Any:
        if args in array:
            print("Getting from cache")
        else:
            print("Calculating new result")
            array[args] = func(*args)
        return array[args]
    return wrapper
