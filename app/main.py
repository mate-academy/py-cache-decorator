from typing import Callable


def cache(func: Callable) -> Callable:
    stor = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in stor:
            print("Calculating new result")
            result = func(*args, **kwargs)
            stor[key] = result
            return result

        print("Getting from cache")
        return stor[key]
    return wrapper
