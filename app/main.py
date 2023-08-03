from functools import wraps
from typing import Callable, ParamSpec, TypeVar

Param = ParamSpec("Param")
RetType = TypeVar("RetType")


def cache(func: Callable[Param, RetType]) -> Callable[Param, RetType]:
    cache_dict: dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> RetType:
        for arg in args:
            try:
                hash(arg)
            except TypeError:
                return func(*args, **kwargs)
        for value in kwargs.values():
            try:
                hash(value)
            except TypeError:
                return func(*args, **kwargs)
        signature: tuple = (args, tuple(kwargs.items()))
        if signature in cache_dict:
            print("Getting from cache")
            return cache_dict[signature]
        print("Calculating new result")
        cache_dict[signature] = func(*args, **kwargs)
        return cache_dict[signature]

    return wrapper
