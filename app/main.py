from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_dict: dict = {}

    def wrapper(*args: Any, **kwargs: Any) -> Callable:
        key: str = str(func.__name__) + str(args) + str(kwargs)
        if key in result_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result_dict[key] = func(*args, **kwargs)
        return result_dict[key]
    return wrapper
