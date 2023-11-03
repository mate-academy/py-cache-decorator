from typing import Callable


def cache(func: Callable) -> Callable:
    catalog_dict = {}

    def wrapper(*args) -> None:

        if args in catalog_dict:
            print("Getting from cache")
            return catalog_dict[args]
        else:
            print("Calculating new result")
            result = func(*args)
            catalog_dict[args] = result
            return result

    return wrapper
