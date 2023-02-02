from typing import Callable, Any


def cache(func: Callable) -> None:
    result_dict = {}

    def wrapper(*args) -> Any:
        if args in result_dict:
            print("Getting from cache")
            return result_dict[args]
        else:
            result_dict.update({args: func(*args)})
            print("Calculating new result")
            return result_dict[args]

    return wrapper
