from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage: dict = {}

    def wrapper(*args: int) -> Any:
        if args in storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            storage[args] = func(*args)
        return storage[args]
    return wrapper
