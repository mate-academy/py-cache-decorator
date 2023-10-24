from typing import Callable


def cache(func: Callable) -> Callable:
    collected_dictionary = {}

    def wrapper(*args, **kwargs) -> dict:
        dict_key = (func, args, frozenset(kwargs.items()))
        if dict_key in collected_dictionary:
            print("Getting from cache")
            return collected_dictionary[dict_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            collected_dictionary[dict_key] = result
            return result
    return wrapper
