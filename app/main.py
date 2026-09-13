from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_dict = {}

    def wrapper(*args: Any) -> Any:
        key = args
        if key in result_dict:
            print("Getting from cache")
            return result_dict[key]
        else:
            print("Calculating new result")
            result_dict[key] = func(*args)
            return result_dict[key]
    return wrapper
