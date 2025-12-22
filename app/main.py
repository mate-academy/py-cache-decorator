from typing import Callable


def cache(func: Callable) -> Callable:
    cashe_dict = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = args, tuple(sorted(kwargs.items()))

        if key not in cashe_dict:
            cashe_dict[key] = func(*args, **kwargs)
            print("Calculating new result")
            return cashe_dict[key]
        else:
            print("Getting from cache")
            return cashe_dict[key]
    return wrapper
