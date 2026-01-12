from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        key = args + tuple(sorted(kwargs.items()))
        if key in result_dict:
            print("Getting from cache")
            return result_dict[key]
        else:
            result = func(*args, **kwargs)
            print("Calculating new result")
            result_dict[key] = result
        return result
    return wrapper
