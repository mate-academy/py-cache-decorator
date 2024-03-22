from typing import Callable


def cache(func: Callable) -> Callable:
    result_cashe = {}


    def wrapper(*args,*kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cashed_result:
            print("Getting from cashe")
            return cashed_result[key]
        else:
            print("Calculating new result")
            result_cashe = func(*args,**kwargs)
            result_cashe = result
            return result

        return wrapper