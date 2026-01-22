from typing import Callable


def cache(func: Callable) -> Callable:
    my_dict = {}

    def wrapper(*args) -> None:
        if args in my_dict:
            print("Getting from cache")
            return my_dict[args]
        else:
            result = func(*args)
            print("Calculating new result")
            my_dict[args] = result
            return result
    return wrapper
