from typing import Callable


def cache(func: Callable) -> Callable:
    empty_dict = {}

    def wrapper(*args, **kwargs) -> any:
        key = (*args, tuple(sorted(kwargs.items())))

        if key in empty_dict:
            print("Getting from cache")
            return empty_dict[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        empty_dict[key] = result
        return result

    return wrapper
