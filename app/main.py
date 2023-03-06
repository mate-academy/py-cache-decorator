from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    completed_runs = {}

    @functools.wraps(func)
    def wrapper(*args) -> Callable:
        if args in completed_runs:
            print("Getting from cache")
        else:
            print("Calculating new result")
            completed_runs.update({args: func(*args)})
        return completed_runs[args]
    return wrapper
