from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args) -> Callable:
        if str(args) in results:
            print("Getting from cache")
            return results[str(args)]
        else:
            print("Calculating new result")
            result = func(*args)
            results[str(args)] = result
            return result

    return wrapper
