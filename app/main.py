from typing import Callable, Any


def cache(in_func: Callable) -> Callable:
    result_dict = {}

    def inner(*args, **kwargs) -> Any:
        kwargs_tuple = tuple(kwargs.items())
        parameters_storage = (args, kwargs_tuple)
        if parameters_storage in result_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result_dict[parameters_storage] = in_func(*args, **kwargs)
        return result_dict[parameters_storage]
    return inner
