from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def decorate(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()))

        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]

        print("Calculating new result")

        result = func(*args, **kwargs)

        cache_storage[key] = result

        return result

    return decorate
