from typing import Callable


def cache(func: Callable) -> Callable:
    storage_dictionary = {}

    def inner_function(*args, **kwargs) -> Callable:
        key = (args, tuple(kwargs.items()))
        if key in storage_dictionary:
            print("Getting from cache")
            return storage_dictionary[key]
        else:
            result = func(*args, **kwargs)
            storage_dictionary[key] = result
            print("Calculating new result")
            return result
    return inner_function
