from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args, **kwargs) -> int:
        key = args + tuple(kwargs.values())

        if key in results.keys():
            print("Getting from cache")
        else:
            print("Calculating new result")
            results[key] = func(*args, **kwargs)

        return results[key]

    return wrapper
