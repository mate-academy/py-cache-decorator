from typing import Callable


def cache(func: Callable) -> Callable:
    def inner(*args, hash_storage=None):
        if hash_storage is None:
            hash_storage = {}
        if args not in hash_storage:
            print("Calculating new result")
            hash_storage[args] = func(*args)
        else:
            print("Getting from cache")
        return hash_storage[args]

    return inner
