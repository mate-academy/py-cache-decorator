from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))

        if key in result_dict:
            print("Getting from cache")
            return result_dict[key]

        result_dict[key] = result = func(*args, **kwargs)
        print("Calculating new result")

        return result

    return wrapper
