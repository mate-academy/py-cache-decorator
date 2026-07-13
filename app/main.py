from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    saved_results = {}

    @wraps(func)
    def wrapper(*args: object, **kwargs: object) -> object:
        arguments = (args, tuple(sorted(kwargs.items())))

        if arguments in saved_results:
            print("Getting from cache")
            return saved_results[arguments]

        print("Calculating new result")
        result = func(*args, **kwargs)
        saved_results[arguments] = result
        return result

    return wrapper
