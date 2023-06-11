from typing import Callable


def cache(func: Callable) -> Callable:
    data_collection = {}

    def inner(*args) -> object:
        if args in data_collection.keys():
            print("Getting from cache")
            return data_collection[args]
        else:
            print("Calculating new result")
            data_collection[args] = func(*args)
        return data_collection[args]
    return inner
