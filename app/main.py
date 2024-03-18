from typing import Callable, Any


def cache(func: Callable) -> Callable:
    temp_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        if args not in temp_dict:
            result = func(*args, **kwargs)
            temp_dict[args] = result
            print("Calculating new result")
            return result

        else:
            print("Getting from cache")
            return temp_dict[args]

    return wrapper
