from typing import Callable


def cache(func: Callable) -> Callable:
    memory = {}

    def wrapper(*args) -> Callable:

        if args in memory:

            print("Getting from cache")
            return memory[args]

        else:
            memory[args] = func(*args)
            print("Calculating new result")
            return memory[args]

    return wrapper
