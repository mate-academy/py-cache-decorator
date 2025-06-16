from typing import Callable


def cache(func: Callable) -> Callable:
    dictionary = {}
    def wrapper(*args, **kwargs) -> Callable:
        key = args + tuple(sorted(kwargs.items()))
        if key in dictionary:
            print("Getting from cache")
            return dictionary[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        dictionary[key] = result
        return result
    return wrapper