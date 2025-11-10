from typing import Callable


def cache(func: Callable) -> Callable:
    memory = {}

    def inner(*args, **kwargs) -> Callable:
        if args not in memory:
            print("Calculating new result")
            memory[args] = func(*args, **kwargs)
            return memory[args]
        else:
            print("Getting from cache")
            return memory[args]

    return inner
