from typing import Callable


def cache(func: Callable) -> Callable:
    dict_of_functions = {}

    def wrapper(*args: object, **kwargs: object) -> object:
        if ((func.__name__, args, frozenset(kwargs.items()))
                in dict_of_functions):
            print("Getting from cache")
        else:
            print("Calculating new result")
            dict_of_functions[
                (func.__name__, args, frozenset(kwargs.items()))
            ] = func(*args, **kwargs)

        return dict_of_functions[
            (func.__name__, args, frozenset(kwargs.items()))
        ]

    return wrapper
