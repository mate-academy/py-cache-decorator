from typing import Callable


def cache(func: Callable) -> Callable:
    memory = dict()

    def wrapper(*args, **kwargs) -> None:
        key = (args, frozenset(kwargs.items()))
        if key not in memory:
            memory[key] = func(*args, **kwargs)
            print("Calculating new result")
            return memory[key]
        else:
            print("Getting from cache")
            return memory[key]
    return wrapper
