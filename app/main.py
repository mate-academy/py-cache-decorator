from typing import Callable, Any


def cache(func: Callable) -> Callable:
    buffer = {}

    def inner(*args) -> Any:
        if args in buffer.keys():
            print("Getting from cache")
            return buffer[args]
        print("Calculating new result")
        result = func(*args)
        buffer[args] = result
        return result

    return inner
