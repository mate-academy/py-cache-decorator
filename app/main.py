from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args, **kwargs) -> int:
        if args in results:
            print("Getting from cache")
            return results[args]
        else:
            print("Calculating new result")
            results[*args] = func(*args, **kwargs)
            return results[args]
    return wrapper
