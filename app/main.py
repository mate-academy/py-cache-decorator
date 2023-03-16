from typing import Any, Callable


def cache(func: Callable) -> Callable:
    memory = {}

    def decorator(*args: tuple, **kwargs: dict) -> Any:
        key = str(args) + str(kwargs)
        if key in memory:
            print("Getting from cache")
            return memory[key]
        value = func(*args, **kwargs)
        memory[key] = value
        print("Calculating new result")
        return memory[key]
    return decorator
