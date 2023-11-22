from typing import Callable


def cache(func: Callable) -> Callable:
    list_of_functions = []
    list_of_results = []

    def wrapper(*args: object, **kwargs: object) -> object:
        if [func.__name__, args, kwargs] in list_of_functions:
            print("Getting from cache")
            return list_of_results[
                list_of_functions.index([func.__name__, args, kwargs])
            ]
        else:
            print("Calculating new result")
            list_of_functions.append([func.__name__, args, kwargs])
            list_of_results.append(func(*args, **kwargs))
            return list_of_results[
                list_of_functions.index([func.__name__, args, kwargs])
            ]

    return wrapper
