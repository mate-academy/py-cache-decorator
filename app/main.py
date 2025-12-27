from typing import Callable


def cache(func: Callable) -> Callable:
    cashe_dict = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = args + tuple(sorted(kwargs.items()))
        if key in cashe_dict:
            print("Getting from cache")
            return cashe_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cashe_dict[key] = result
            return result
    return wrapper
