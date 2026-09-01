from typing import Callable


def cache(func: Callable) -> Callable:
    func.cache = {}

    def wrapper(*args, **kwargs) -> int:
        key = str(args)
        if key not in func.cache:
            func.cache[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return func.cache[key]
    return wrapper
