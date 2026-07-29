from typing import Callable


def cache(func: Callable) -> Callable:
    cached_functions = {}

    def inner(*args, **kwargs) -> Callable:
        str_arguments = str(args) + str(kwargs)
        if str_arguments not in cached_functions:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_functions[str_arguments] = result
            return result
        else:
            print("Getting from cache")
            return cached_functions[str_arguments]

    return inner
