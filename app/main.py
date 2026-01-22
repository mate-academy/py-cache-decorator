from typing import Callable, Any


def cache(func: Callable) -> Callable:
    data_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        key = args + tuple(sorted(kwargs.items()))
        if key in data_dict:
            print("Getting from cache")
            return data_dict[key]
        data_dict[key] = func(*args, **kwargs)
        print("Calculating new result")
        return data_dict[key]
    return wrapper
