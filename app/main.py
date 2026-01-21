from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result: dict = {}

    def inner(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in result:
            print("Getting from cache")
            return result[key]
        else:
            print("Calculating new result")
            function = func(*args, **kwargs)
            result[key] = function
            return function
    return inner
