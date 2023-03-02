from typing import Callable


def cache(func: Callable) -> None:

    completed_runs = {}

    def inner(*args) -> str:
        if args in completed_runs:
            print("Getting from cache")
        else:
            print("Calculating new result")
            completed_runs[args] = func(*args)

        return completed_runs[args]

    return inner
