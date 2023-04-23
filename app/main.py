from typing import Callable, Any


def cache(func: Callable) -> Callable:
    previous_value = {}

    def wrapper(*args, **kwargs) -> Any:
        if args in previous_value:
            print("Getting from cache")
        else:
            print("Calculating new result")
            previous_value[args] = func(*args)

        return previous_value[args]
    return wrapper
