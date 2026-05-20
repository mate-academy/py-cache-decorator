from typing import Callable


def cache(func: Callable) -> Callable:
    memory = {}
    def wrapper(*args, **kwargs):
        key = (args,tuple(kwargs.items()))
        if key in memory:
            print("Getting from cache")
            return memory[key]
        elif key not in memory:
            print("Calculating new result")
            result = func(*args, **kwargs)
            memory[key] = result
            return result
    return wrapper
