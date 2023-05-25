from typing import Callable


def cache(func: Callable) -> Callable:
    stored_results = dict()

    def wrapper(*args) -> Callable:

        if args in stored_results:
            print("Getting from cache")
            return stored_results[args]
        else:
            new_result = func(*args)
            stored_results[args] = new_result
            print("Calculating new result")
            return new_result
    return wrapper
