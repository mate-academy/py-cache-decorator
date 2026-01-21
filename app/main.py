from typing import Callable, Any


def cache(func: Callable) -> Callable:
    check_dict = {}
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in check_dict:
            print("Getting from cache")
            return check_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            check_dict[key] = result
            return result
    return wrapper
