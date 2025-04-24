from typing import Callable


def cache(func: Callable) -> Callable:
    known_results = {}

    def wrapper(*args) -> Callable:
        if args in known_results:
            print("Getting from cache")
            return known_results[args]
        else:
            print("Calculating new result")
            result = func(*args)
            known_results[args] = result
            return result

    return wrapper
