from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args, **kwargs) -> Any:
        if (*args, tuple(**kwargs)) not in result:
            result[(*args, tuple(**kwargs))] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return result[(*args, tuple(**kwargs))]

    return wrapper
