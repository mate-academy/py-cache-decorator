from typing import Callable


def cache(func: Callable) -> Callable:
    stored_result = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key in stored_result:
            print("Getting from cache")
            return stored_result[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        stored_result[key] = result
        return result

    return wrapper
