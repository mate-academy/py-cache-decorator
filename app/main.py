from typing import Callable, Any


def cache(func: Callable) -> Any:

    result_dict = {}

    def wrapper(*args: tuple) -> Any:

        if args not in result_dict:
            print("Calculating new result")
            result_dict[args] = func(*args)
            return result_dict[args]

        print("Getting from cache")
        return result_dict.get(args)
    return wrapper
