from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args, **kwargs) -> dict:
        function_argument = args + tuple(kwargs.values())
        if function_argument not in storage:
            storage[function_argument] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return storage[function_argument]
    return wrapper
