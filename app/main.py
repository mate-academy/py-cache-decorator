from typing import Any, Callable
import functools


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def check(name: str, args: tuple) -> bool:
        if name not in cache_dict:
            return False
        elif args not in cache_dict.get(name):
            return False
        else:
            return True

    def set(name: str, args: tuple, value: Any) -> None:
        if name not in cache_dict:
            cache_dict.update({name: {args: value}})
        else:
            cache_dict.get(name).update({args: value})

    def get(name: str, args: tuple) -> Any:
        return cache_dict.get(name).get(args)

    @functools.wraps(func)
    def inner(*args, **kwargs) -> Any:
        name = func.__name__
        args_tuple = args, frozenset(kwargs)

        if check(name, args_tuple):
            print("Getting from cache")
            return get(name, args_tuple)
        else:
            print("Calculating new result")
            value = func(*args, **kwargs)
            set(name, args_tuple, value)

            return value

    return inner
