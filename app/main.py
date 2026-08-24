from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage: dict = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = args
        if key in storage:
            print("Getting from cache")
            return storage[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        storage[key] = result
        return result

    return wrapper
