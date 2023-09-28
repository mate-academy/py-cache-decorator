from typing import Callable


def cache(func: Callable) -> Callable:
    run_results = {}

    def wrapper(*args) -> Callable:
        if args not in run_results:
            run_results[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return run_results[args]

    return wrapper
