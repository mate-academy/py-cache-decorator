from typing import Callable


def cache(func: Callable) -> Callable:
    cached = {}

    def wrapper(*args, **kwargs) -> None:
        items = str(args)
        if items not in cached:
            result = func(*args, **kwargs)
            cached[items] = result
            print("Calculating new result")
            return result
        elif items in cached:
            print("Getting from cache")
            return cached[items]
        return None
    return wrapper
