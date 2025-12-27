from typing import Callable, Any


def cache(func: Callable) -> Callable:
    memory = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (*args, *kwargs.items())
        result = memory.get(key)
        if result is None:
            print("Calculating new result")
            result = func(*args, **kwargs)
            memory[key] = result
        else:
            print("Getting from cache")
        return result

    return wrapper
