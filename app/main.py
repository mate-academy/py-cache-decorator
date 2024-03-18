from typing import Callable


def cache(func: Callable) -> Callable:
    memory = {}

    def wrapper(*args) -> None:
        if args in memory:
            print("Getting from cache")
            return memory[args]
        else:
            print("Calculating new result")
            result = func(*args)
            memory[args] = result
            return result
    return wrapper
