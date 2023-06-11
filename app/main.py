from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    data_collection = {}

    @wraps(func)
    def inner(*args) -> object:
        if args in data_collection.keys():
            print("Getting from cache")
        else:
            print("Calculating new result")
            data_collection[args] = func(*args)
        return data_collection[args]
    return inner
