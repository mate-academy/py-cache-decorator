from typing import Callable


def cache(func: Callable) -> Callable:
    data_collection = {}

    def inner(*args) -> object:
        if args in data_collection.keys():
            print("Getting from cache")
            return data_collection[args]
        else:
            print("Calculating new result")
            data = func(*args)
            data_collection[args] = data
            return data
    return inner
