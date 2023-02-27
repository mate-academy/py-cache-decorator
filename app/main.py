from typing import Any
from typing import Callable


def cache(func: Callable) -> None:
    storage = {}

    def wrapper(*args: Any) -> Any:
        if args in storage.keys():
            print("Getting from cache")
        else:
            print("Calculating new result")
            storage[args] = func(*args)

        return storage[args]

    return wrapper
