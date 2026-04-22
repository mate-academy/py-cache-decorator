from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args: Any) -> Any:
        if args in storage:
            print("Getting from cache")
            return storage[args]

        print("Calculating new result")
        res = func(*args)
        storage[args] = res
        return res
    return wrapper
