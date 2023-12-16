from typing import Callable


def cache(func: Callable) -> Callable:
    all_result = {}

    def wrapper(*args, **kwargs) -> None:
        key = (args, frozenset(kwargs.items()))

        if key in all_result:
            print("Getting from cache")
            return all_result[key]
        else:
            result = func(*args, **kwargs)
            all_result[key] = result
            print("Calculating new result")
            return result

    return wrapper
