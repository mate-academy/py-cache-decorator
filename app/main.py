from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def inner(*args) -> Any:
        arguments = args
        if arguments not in cache_storage:
            print("Calculating new result")
            value = func(*args)
            cache_storage[arguments] = value
            return value
        else:
            print("Getting from cache")
            value = cache_storage[arguments]
            return value
    return inner
