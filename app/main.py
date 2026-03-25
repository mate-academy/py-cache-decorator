from typing import Callable


def cache(func: Callable) -> Callable:
    saved_results = {}

    def wrapper(*args) -> Callable:
        if args in saved_results:
            print("Getting from cache")
            return saved_results[args]

        print("Calculating new result")
        result = func(*args)
        saved_results[args] = result
        return result

    return wrapper
