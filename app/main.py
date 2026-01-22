from typing import Callable


def cache(func: Callable) -> Callable:
    kesh = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (tuple(args), tuple(sorted(kwargs.items())))
        if key in kesh:
            print("Getting from cache")
            return kesh[key]
        else:
            res = func(*args, **kwargs)
            kesh[key] = res
            print("Calculating new result")
            return res
    return wrapper
