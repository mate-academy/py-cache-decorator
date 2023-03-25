from typing import Callable


def cache(func: Callable) -> Callable:
    stored_values = {}

    def inner(*args: Callable) -> int:
        keys = args
        if keys not in stored_values.keys():
            result = func(*args)
            stored_values[keys] = result
            print("Calculating new result")
            return result

        print("Getting from cache")
        return stored_values[keys]

    return inner
