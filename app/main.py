from typing import Any, Callable


def cache(func: Callable) -> Callable:
    result = {}

    def inner(*args, **kwargs) -> Any:
        key = str(args) + str(kwargs)
        if key in result:
            print("Getting from cache")
            return result[key]

        print("Calculating new result")
        result[key] = func(*args, **kwargs)
        return result[key]

    return inner
