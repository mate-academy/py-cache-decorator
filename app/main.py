from typing import Callable


def cache(in_func: Callable) -> Callable:
    result_dict = {}

    def inner(*args, **kwargs) -> Callable:
        kwargs_tuple = tuple(kwargs.items())
        if (args, kwargs_tuple) in result_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result_dict[(args, kwargs_tuple)] = in_func(*args, **kwargs)
        return result_dict[(args, kwargs_tuple)]
    return inner
