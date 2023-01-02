from typing import Callable, Any


def cache(func: Callable) -> Callable:
    dict_of_date = {}

    def wrapper(*args) -> Any:
        if args not in dict_of_date.keys():
            print("Calculating new result")
            dict_of_date[args] = func(*args)
        else:
            print("Getting from cache")
        return dict_of_date[args]

    return wrapper
