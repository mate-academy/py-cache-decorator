from typing import Callable


def cache(func: Callable) -> Callable:
    data = []

    def wrapper(*args, **kwargs) -> tuple:
        if args in data:
            print("Getting from cache")
            return args[0]
        data.append(args)
        print("Calculating new result")
        return func(*args, **kwargs)
    return wrapper
