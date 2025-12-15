from typing import Callable, Any


def cache(func: Callable) -> Callable:
    dictionary = {}

    def inner(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in dictionary:
            print("Getting from cache")
            return dictionary[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            dictionary[key] = result
            return result
    return inner

