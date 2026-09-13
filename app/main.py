from typing import Callable, Any


def cache(func: Callable) -> Callable:
    def wrapper(*args: Any, result_dict: dict = {}) -> Any:
        key = args
        if key in result_dict:
            print("Getting from cache")
            return result_dict[key]
        else:
            print("Calculating new result")
            result_dict[key] = func(*args)
            return result_dict[key]
    return wrapper
