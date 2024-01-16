from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = {}

    def repeat_function(*args) -> Any:
        if args in results:
            print("Getting from cache")
            return results[args]
        else:
            print("Calculating new result")
            new_result = func(*args)
            results[args] = new_result
            return new_result
    return repeat_function
