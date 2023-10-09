from typing import Callable


def cache(func: Callable) -> Callable:
    def inner(*args, **kwargs) -> None:

    return inner


@cache
def long_time_func(*args, **kwargs) -> None:
