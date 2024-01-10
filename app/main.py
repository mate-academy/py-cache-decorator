from typing import Callable


def cache(func: Callable) -> Callable:
    memory = {}

    def inner(*args) -> dict:
        if args in memory.keys():
            print("Getting from cache")
        else:
            print("Calculating new result")
            memory[args] = func(*args)
        return memory[args]
    return inner
