from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    catalog_dict = {}

    @wraps(func)
    def wrapper(*args) -> None:

        if args in catalog_dict:
            print("Getting from cache")

        else:
            print("Calculating new result")
            catalog_dict[args] = func(*args)
        return catalog_dict[args]

    return wrapper
