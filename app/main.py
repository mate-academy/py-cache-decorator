from typing import Callable


def cache(func: Callable) -> Callable:
    result_cashe = {}


    def wrapper(*args,**kwargs):
        nonlocal result_cashe
        key = (args, frozenset(kwargs.items()))
        if key in result_cashe:
            print("Getting from cashe")
            return result_cashe[key]
        else:
            print("Calculating new result")
            result = func(*args,**kwargs)
            result_cashe[key] = result
            return result

    return wrapper
