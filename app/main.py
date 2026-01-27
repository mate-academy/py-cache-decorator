from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    previous_runs = dict()

    @functools.wraps(func)
    def wrapper(*args) -> Any:
        if args not in previous_runs.keys():
            print("Calculating new result")
            result = func(*args)
            previous_runs[args] = result
        else:
            print("Getting from cache")
            result = previous_runs[args]
        return result

    return wrapper
