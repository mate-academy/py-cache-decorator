from typing import Callable, Any


def cache(func: Callable, hash_storage: dict = None) -> Callable:
    if hash_storage is None:
        hash_storage = {}

    def inner(*args) -> Any:
        storage_key = (func.__name__, args)
        if storage_key not in hash_storage:
            print("Calculating new result")
            hash_storage[storage_key] = func(*args)
        else:
            print("Getting from cache")
        return hash_storage[storage_key]

    return inner
