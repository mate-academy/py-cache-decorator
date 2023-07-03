from typing import Callable


result_args_dict = {}


def cache(func: Callable) -> Callable:
    def inner(*args) -> None:
        if func.__name__ in result_args_dict:
            if args in result_args_dict[func.__name__]:
                print("Getting from cache")
                return result_args_dict[func.__name__][args]
            else:
                value = func(*args)
                result_args_dict[func.__name__][args] = value
                print("Calculating new result")
                return value
        else:
            value = func(*args)
            result_args_dict[func.__name__] = {}
            result_args_dict[func.__name__][args] = value
            print("Calculating new result")
            return value
    return inner
