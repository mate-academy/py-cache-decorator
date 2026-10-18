from typing import Any, Callable


def cache(func: Callable) -> Callable:
    memory = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in memory:
            print("Getting from cache")
            return memory[key]
        print("Calculating new result")
        memory[key] = func(*args, **kwargs)
        return memory[key]

    return wrapper
