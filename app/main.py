from typing import Callable


def cache(func: Callable) -> Callable:
    dictionary = {}

    def wrapper(*args) :
        if args in dictionary:
            print("Getting from cache")
            return dictionary[args]
        print("Calculating new result")
        result = func(*args)
        dictionary[args] = result
        return result
    return wrapper
