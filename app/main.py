from typing import Callable


def cache(func) -> Callable:
    res_dict = {}

    def inner(*args, **kwargs) -> Callable:
        if f"{args}" in res_dict:
            print("Getting from cache")
            return res_dict[f"{args}"]
        else:
            func(*args)
            res_dict[f"{args}"] = func(*args)
            print("Calculating new result")
        return func
    return inner
