from typing import Callable


def cache(func: Callable):
    stored_results = {}
    def wrapper(*args):
        if args in stored_results:
            print("Getting from cache")
            return stored_results[args]
        print("Calculating new result")
        result = func(*args)
        stored_results[args] = result
        return result
    return wrapper
