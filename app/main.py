from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:

    result_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> dict:
        if args in result_dict:
            print("Getting from cache")
            return result_dict[args]

        print("Calculating new result")

        resultat = func(*args)
        result_dict[args] = resultat

        return resultat

    return wrapper
