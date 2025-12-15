import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    memory = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        total_data = (args, tuple(kwargs.items()))
        if total_data not in memory:
            memory[total_data] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return memory[total_data]

    return wrapper


def getting_from_cache(*args, **kwargs) -> str:
    return f"{args}, {kwargs}"
