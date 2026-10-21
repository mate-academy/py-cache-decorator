from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args) -> int:
        if args in results:
            print("Getting from cache")
            return results[args]
        print("Calculating new result")
        result = func(*args)
        results[args] = result
        return result
    return wrapper
