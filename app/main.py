from typing import Callable


def cache(func: Callable) -> Callable:
    dict1 = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = args
        if key in dict1:
            print("Getting from cache")
            return dict1[key]
        else:
            result = func(*args, **kwargs)
            dict1[key] = result
            print("Calculating new result")
            return result

    return wrapper
