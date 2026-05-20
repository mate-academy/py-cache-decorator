from typing import Callable, Any


def cache(func: Callable) -> Callable:
    memory = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()))

        if key in memory:
            print("Getting from cache")
            return memory[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        memory[key] = result
        return result
    return wrapper
