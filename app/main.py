from typing import Callable


def cache(func: Callable) -> Callable:

    result = {}
    def inner(*args):
        if tuple(args) in result.keys():
            print("Getting from cache")
            return result[tuple(args)]
        else:
            result[tuple(args)] = func(*args)
            print("Calculating new result")
            return result[tuple(args)]
    
    return inner
