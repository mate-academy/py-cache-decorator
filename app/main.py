from typing import Callable


def cache(func: Callable) -> Callable:
    memory_dict = {}

    def wrapper(*args) -> int:
        if args in memory_dict:
            print("Getting from cache")
            return memory_dict[args]
        else:
            print("Calculating new result")
            result = func(*args)
            memory_dict[args] = result
            return result
    return wrapper
