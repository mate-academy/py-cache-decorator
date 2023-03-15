from typing import Callable


def cache(func: Callable) -> Callable:
    memory = {}

    def decorator(*args, **kwargs) -> Callable:
        key = str(args) + str(kwargs)
        if key in memory:
            print("Getting from cache")
            return memory[key]
        else:
            value = func(*args, **kwargs)
            memory[key] = value
            print("Calculating new result")
            return memory[key]
    return decorator
