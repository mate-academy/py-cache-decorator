from typing import Any, Callable


def cache(func: Callable) -> Callable:
    memory = {}

    def decorator(*args: tuple, **kwargs: dict) -> Any:
        key = args
        if key in memory:
            print("Getting from cache")
            return memory[key]
        memory[key] = func(*args, **kwargs)
        print("Calculating new result")
        return memory[key]
    return decorator
