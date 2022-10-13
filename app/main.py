from typing import Callable


def cache(func) -> Callable:
    res_dict = {}

    def inner(*args, **kwargs):
        if f"{args}" in res_dict:
            print("Getting from cache")
        else:
            res_dict[f"{args}"] = func(*args)
            print("Calculating new result")
    return inner
