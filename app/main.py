from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_dict = {}

    def wrapper(*args) -> Any:
        if args in result_dict:
            print("Getting from cache")
            return result_dict.get(args)
        else:
            result = func(*args)
            result_dict.update({args: result})
            print("Calculating new result")
            return result

    return wrapper
