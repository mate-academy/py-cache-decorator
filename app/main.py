from typing import Callable, Any


def cache(func: Callable) -> Callable:
    memory = {}

    def inner(*args) -> Any:
        if args in memory:
            print("Getting from cache")
        else:
            print("Calculating new result")
            memory[args] = func(*args)
        return memory[args]
    return inner
