from typing import Any, Callable


def cache(func: Callable) -> Callable:
    memory = {}

    def wrapper(*args) -> Any:
        if args in memory:
            print("Getting from cache")
            return memory.get(args)
        else:
            result = func(*args)
            memory[args] = result
            print("Calculating new result")
            return result

    return wrapper
