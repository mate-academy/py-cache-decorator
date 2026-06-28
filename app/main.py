from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args: int) -> int:
        if args in result:
            print("Getting from cache")
            return result[args]
        else:
            print("Calculating new result")
            results_ = func(*args)
            result[args] = results_
            return results_
    return wrapper
