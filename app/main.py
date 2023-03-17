from typing import Callable, Any


def cache(func: Callable) -> None:
    memory = {}

    def wrapper(*args: Any) -> None:
        if args in memory:
            print("Getting from cache")
            return memory[args]
        else:
            memory[args] = func(*args)
            print("Calculating new result")
            return memory[args]

    return wrapper
