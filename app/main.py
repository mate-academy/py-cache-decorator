from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args, **kwargs) -> str:
        key = str(args)
        if key not in result:
            print("Calculating new result")
            new_result = func(*args, **kwargs)
            result[key] = new_result
        else:
            print("Getting from cache")
            return result[key]
        return new_result
    return wrapper
