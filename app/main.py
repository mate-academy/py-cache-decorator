from typing import Callable


def cache(func: Callable) -> Callable:
    data = {}

    def wrapper(*args, **kwargs) -> Callable:
        if args in data:
            print("Getting from cache")
            result = data.get(args)
        else:
            result = func(*args, **kwargs)
            print("Calculating new result")
            data[args] = result

        return result

    return wrapper
