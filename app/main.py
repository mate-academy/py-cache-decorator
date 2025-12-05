from typing import Callable


def cache(func: Callable) -> Callable:
    stored_result = {}

    def wrapper(*args):
        if args in stored_result:
            print("Getting from cache")
            return stored_result[args]
        print("Calculating new result")
        result = func(*args)
        stored_result[args] = result
        return result

    return wrapper
