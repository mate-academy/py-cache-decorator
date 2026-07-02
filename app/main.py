from typing import Callable


def cache(func: Callable) -> Callable:
    cached = {}

    def wrapper(*args, **kwargs) -> Callable:
        cur_args = str(args)
        cur_args += " ".join(
            [f"{key}={value}" for key, value in kwargs.items()]
        )
        if cur_args in cached:
            print("Getting from cache")
            return cached[cur_args]
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
            cached[cur_args] = res
            return res
    return wrapper
