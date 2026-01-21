from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    store = {}
    _kw_mark = object()

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        if kwargs:
            key = args + (_kw_mark,) + tuple(sorted(kwargs.items()))
        else:
            key = args

        try:
            hash(key)
        except TypeError:
            raise TypeError("cache decorator supports only hashable arguments")

        if key in store:
            print("Getting from cache")
            return store[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        store[key] = result
        return result

    return wrapper
