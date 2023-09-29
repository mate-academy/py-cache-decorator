from typing import Callable, Any


def cache(func: Callable) -> Callable:
    run_results = {}

    def wrapper(*args) -> Any:
        if args not in run_results:
            run_results[args] = func(*args)
            print("Calculating new result")
            return run_results[args]
        print("Getting from cache")
        return run_results[args]

    return wrapper
