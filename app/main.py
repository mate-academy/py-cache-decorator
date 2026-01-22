from typing import Callable


def cache(func: Callable) -> Callable:
    completed_runs = {}

    def wrapper(*args) -> list:

        if args in completed_runs:
            print("Getting from cache")
        else:
            print("Calculating new result")
            completed_runs.update({args: func(*args)})

        return completed_runs[args]

    return wrapper
