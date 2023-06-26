from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    def inner(*args) -> Any:

        if args in storage:
            print("Getting from cache")
            result = storage[args]
        else:
            result = func(*args)
            print("Calculating new result")
            storage[args] = result
        return result

    return inner
