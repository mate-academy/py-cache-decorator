from typing import Callable


def cache(func: Callable) -> Callable:

    result_storage = {}

    def wrapper(*args, **kwargs) -> int:
        if args in result_storage:
            print("Getting from cache")
            return result_storage[args]
        else:
            result_storage[args] = func(*args, **kwargs)
            print("Calculating new result")
            return result_storage[args]
    return wrapper
