from typing import Callable, Any


def cache(func: Callable) -> Callable:
    saved_data = {}

    def wrapper(*args: tuple, **kwargs: dict) -> Any:
        if args not in saved_data:
            print("Calculating new result")
            saved_data[args] = saved_data.get(args, func(*args, **kwargs))
        else:
            print("Getting from cache")
        return saved_data[args]

    return wrapper
