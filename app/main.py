from typing import Callable, Any


def cache(func: Callable) -> Any:
    memory = {}

    def wrapper(*args: Any) -> str:
        if args in memory:
            print("Getting from cache")

        else:
            memory[args] = func(*args)
            print("Calculating new result")
        return memory[args]

    return wrapper
