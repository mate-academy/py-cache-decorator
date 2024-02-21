from typing import Callable


def cache(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))

        if key in wrapper.cache_storage:
            print("Getting from cache")
            return wrapper.cache_storage[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        wrapper.cache_storage[key] = result
        return result

    wrapper.cache_storage = {}
    return wrapper