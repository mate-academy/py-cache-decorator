from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_archive = {}

    def inner(*args, **kwargs) -> Any:
        key = args + tuple(kwargs.items())
        if key not in result_archive:
            print("Calculating new result")
            result_archive[args] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return result_archive[key]
    return inner
