from typing import Callable


def cache(func: Callable) -> Callable:
    data = {}

    def wrapper(*args, **kwargs) -> int:
        if args in data:
            print("Getting from cache")
            return data[args]
        print("Calculating new result")
        result = func(*args, **kwargs)
        data.update({args: result})
        return result
    return wrapper
