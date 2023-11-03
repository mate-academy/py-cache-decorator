from typing import Callable, Any


def cache(func: Callable) -> Callable:
    data = {}

    def inner(*args: Any) -> Callable:
        key = (args)
        if key in data:
            print("Getting from cache")
            result = data[key]
        else:
            result = func(*args)
            print("Calculating new result")
            data[key] = result
        return result

    return inner
