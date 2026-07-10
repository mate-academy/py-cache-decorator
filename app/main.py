from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage: dict = {}

    def wrapper(arg1: Any, arg2: Any, *args) -> Callable:
        if (arg1, arg2, args) in storage:
            print("Getting from cache")
            return storage[arg1, arg2, args]
        else:
            print("Calculating new result")
            storage[arg1, arg2, args] = func(arg1, arg2, *args)
            return storage[arg1, arg2, args]
    return wrapper
