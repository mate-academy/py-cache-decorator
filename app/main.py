from typing import Callable, Any


def cache(func: Callable) -> Any:
    my_dictionary = {}

    def wrapper(*args: Callable) -> Any:
        if args in my_dictionary:
            print("Getting from cache")
        else:
            result = func(*args)
            my_dictionary[args] = result
            print("Calculating new result")
        return my_dictionary[args]
    return wrapper
