from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache = {}

    def compute_key(args: tuple, kwargs: dict) -> str:
        arg_str = ",".join(str(arg) for arg in args)
        kwarg_str = ",".join(f"{key}={value}" for key, value in kwargs.items())
        key = arg_str + kwarg_str
        return key

    def wrapper(*args, **kwargs) -> Any:
        key = compute_key(args, kwargs)
        if key in cache:
            print("Getting from cache")
            return cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache[key] = result
            return result

    return wrapper
