from typing import Callable


def cache(func: Callable) -> Callable:
    memory = {}

    def wrapper(*args, **kwargs) -> str:
        if args not in memory:
            memory[args] = func(*args, **kwargs)
            print("Calculating new result")
            return memory[args]
        else:
            print("Getting from cache")
            return memory[args]

    return wrapper
