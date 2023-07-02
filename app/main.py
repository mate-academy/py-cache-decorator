from typing import Callable, Any


def cache(func: Callable) -> Callable:
    data = {}

    def wrapper(*args: Any) -> Any:
        if args not in data.keys():
            data[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return data[args]

    return wrapper
