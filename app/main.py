from typing import Callable


def cache(func: Callable) -> Callable[[dict[str]], int]:
    res_dict = {}

    def inner(*args, **kwargs) -> int:
        if f"{args}" in res_dict:
            print("Getting from cache")
        else:
            res_dict[f"{args}"] = func(*args)
            print("Calculating new result")
        return res_dict[f"{args}"]
    return inner
