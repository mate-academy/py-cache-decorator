from typing import Callable


def cache(func: Callable) -> Callable:
    saved_results = {}

    def wrapper(*args) -> any:
        if args not in saved_results:
            print("Calculating new result")
            saved_results[args] = func(*args)
            return saved_results[args]
        else:
            print("Getting from cache")
            for cached in saved_results:
                if cached == args:
                    return saved_results[args]
    return wrapper
