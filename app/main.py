from typing import Callable


def cache(func: Callable) -> Callable:
    dict_cache = {}

    def wrapper(*args, **kwargs) -> None:

        if args in dict_cache:
            print("Getting from cache")
            return dict_cache[args]
        else:
            print("Calculating new result")

        result = func(*args, **kwargs)
        dict_cache[args] = result

        return result

    return wrapper
