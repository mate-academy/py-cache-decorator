from typing import Callable


def cache(func: Callable) -> Callable:
    result_dict = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))

        if key in result_dict:
            print("Getting from cache")
            return result_dict[key]

        result = func(*args, **kwargs)
        result_dict[key] = result
        print("Calculating new result")

        return result

    return wrapper
