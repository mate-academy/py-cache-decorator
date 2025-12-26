from typing import Callable, Any


def cache(func: Callable) -> Callable:
    memory = {}

    def inner(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key not in memory:
            print("Calculating new result")
            memory[key] = func(*args, **kwargs)
            return memory[key]
        else:
            print("Getting from cache")
            return memory[key]

    return inner
