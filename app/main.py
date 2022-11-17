from typing import Callable, Any


def cache(func: Callable) -> Callable:
    buffer = {}

    def inner(*args: Any) -> Any:
        if args in buffer:
            print("Getting from cache")
            return buffer[args]

        if args not in buffer:
            print("Calculating new result")
            buffer[args] = func(*args)
            return buffer[args]

    return inner
