from typing import Callable


def cache(func: Callable) -> Callable:
    stored_runs = {}

    def wrapper(*args):
        if args in stored_runs:
            print("Getting from cache")
            return stored_runs[args]
        print("Calculating new result")
        stored_runs.update({args: func(*args)})
        return stored_runs[args]
    return wrapper
