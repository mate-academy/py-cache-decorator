from typing import Callable, Any

dictionary = {}


def cache(func: Callable) -> Any:

    def inner(*args, **kwargs) -> Any:
        key = func, args
        if key in dictionary:
            print("Getting from cache")
            return dictionary[key]
        result = func(*args, **kwargs)
        dictionary[key] = result
        print("Calculating new result")
        return result
    return inner
