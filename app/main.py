from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    results: dict = {}

    @wraps(func)
    def wrapper(*args: (int, float, str, tuple)) -> dict:
        if args in results:
            print("Getting from cache")
            return results[args]

        print("Calculating new result")
        result = func(*args)
        results[args] = result
        return result

    return wrapper
