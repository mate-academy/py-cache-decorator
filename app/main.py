from typing import Callable


def cache(func: Callable) -> Callable:
    dict_cache = {}

    def inner(*args, **kwargs) -> tuple:
        inputs = (*args, *kwargs.values())
        if inputs not in dict_cache:
            result = func(*args)
            dict_cache[inputs] = result
            print("Calculating new result")
            return result
        print("Getting from cache")
        return dict_cache[inputs]
    return inner
