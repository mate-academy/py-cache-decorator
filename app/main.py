from typing import Callable

memory = {}


def cache(func: Callable) -> Callable:
    def inner(*args, **kwargs) -> dict:
        key = args + tuple(kwargs.items()), func
        if key not in memory:
            memory[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return memory[key]

    return inner
