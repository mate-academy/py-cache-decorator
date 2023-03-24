from typing import Callable, Any


def cache(func: Callable) -> Any:
    data_dict = {}

    def inner(*args) -> Any:
        if args in data_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            data_dict[args] = func(*args)
        return data_dict[args]

    return inner
