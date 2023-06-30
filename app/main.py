from functools import wraps
from typing import Callable


def cache(func: Callable) -> None:
    results: dict = {}

    @wraps(func)
    def wrapper(*args: any) -> any:
        if args in results:
            print("Getting from cache")
            return results[args]
        else:
            print("Calculating new result")
            result = func(*args)
            results[args] = result
            return result

    return wrapper
