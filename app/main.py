from typing import Callable, Any


def cache(func: Callable) -> Callable:
    memory_dict = {}

    def wrapper(*args: Any) -> Callable:
        if args not in memory_dict:
            print("Calculating new result")
            memory_dict[args] = func(*args)
            return memory_dict[args]
        else:
            print("Getting from cache")
            return memory_dict[args]

    return wrapper
