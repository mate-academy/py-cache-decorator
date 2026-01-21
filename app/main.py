from typing import Callable


def cache(func: Callable) -> Callable:
    stored_res = {}
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key in stored_res:
            return stored_res[key]
        res = func(*args, **kwargs)
        stored_res[key] = res
        return res
    return wrapper
