from typing import Callable, Any


def cache(func: Callable) -> Callable:
    buffer = {}

    def wrapper(*args) -> Any:
        if args in buffer:
            print("Getting from cache")
            return buffer[args]
        else:
            print("Calculating new result")
            res = func(*args)
            buffer[args] = res
            return res

    return wrapper
