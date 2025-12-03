from typing import Any, Callable
import functools


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def check(args: tuple) -> bool:
        if args not in cache_dict:
            return False
        else:
            return True

    def set(args: tuple, value: Any) -> None:
        cache_dict.update({args: value})

    def get(args: tuple) -> Any:
        return cache_dict.get(args)

    @functools.wraps(func)
    def inner(*args, **kwargs) -> Any:
        args_tuple = args, frozenset(kwargs.items())

        if check(args_tuple):
            print("Getting from cache")
            return get(args_tuple)
        else:
            print("Calculating new result")
            value = func(*args, **kwargs)
            set(args_tuple, value)

            return value

    return inner
