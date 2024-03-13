from typing import Callable, Any


def cache(func: Callable) -> Callable:
    hash_storage = {}

    def inner(*args) -> Any:
        if args not in hash_storage:
            print("Calculating new result")
            hash_storage[args] = func(*args)
        else:
            print("Getting from cache")
        return hash_storage[args]

    return inner
