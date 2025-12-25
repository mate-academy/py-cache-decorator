from typing import Callable, Any


def cache(func: Callable) -> Callable:
    change_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in change_dict:
            print("Getting from cache")
            return change_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            change_dict[key] = result

        return result
    return wrapper
