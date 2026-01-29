from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_dict = {}

    def inner(*args, **kwargs) -> Any:
        if args in result_dict:
            print("Getting from cache")
            return result_dict[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            result_dict[args] = result
            return result

    return inner
