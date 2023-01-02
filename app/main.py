from typing import Callable, Any


def cache(func: Callable) -> Callable:
    dict_of_date = {}

    def wrapper(*args) -> Any:
        if args in dict_of_date.keys():
            print("Getting from cache")
            return dict_of_date.get(args)
        else:
            dict_of_date[args] = func(*args)
            print("Calculating new result")
            return dict_of_date[args]

    return wrapper
