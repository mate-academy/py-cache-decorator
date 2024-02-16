from typing import Callable


def cache(func: Callable) -> Callable:
    results_value_cashe = {}

    def wrapper_function(*args, **kwargs) -> Callable:
        key = (args, frozenset(kwargs.items()))
        if key in results_value_cashe:
            print("Getting from cache")
            return results_value_cashe[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            results_value_cashe[key] = result
            return result
    return wrapper_function
