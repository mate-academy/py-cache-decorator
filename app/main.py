from typing import Callable, Any


def cache(func: Callable) -> Callable:
    data = {}

    def wrapper(*args, **kwargs) -> Any:

        if args in data:
            print("Getting from cache")
            return data[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            data[args] = result
            return result

    return wrapper
