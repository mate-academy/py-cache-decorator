from typing import Callable


def cache(func: Callable) -> Callable:
    list1 = {}
    def wrapper(*args, **kwargs) -> dict:
        key = (args, tuple(sorted(kwargs.items())))
        if key in list1:
            print("Getting from cache")
        else:
            list1[key] = func(*args, **kwargs)
            print("Calculating new result")
        return list1[key]
    return wrapper