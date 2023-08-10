from typing import Callable


def cache(func: Callable) -> Callable:
    previous_runs = {}

    def inner(*args) -> object:
        if args in previous_runs.keys():
            print("Getting from cache")
            return previous_runs[args]
        print("Calculating new result")
        result = func(*args)
        previous_runs[args] = result
        return result

    return inner
