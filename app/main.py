from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results_of_function_runs = {}

    def inner(*args) -> Any:
        if args not in results_of_function_runs:
            result = func(*args)
            results_of_function_runs[args] = result
            print("Calculating new result")
            return result
        else:
            print("Getting from cache")
            return results_of_function_runs[args]
    return inner
