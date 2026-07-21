from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    def inner(*args, **kwargs) -> Any:
        data = (args, tuple(sorted(kwargs.items())))

        if data in storage:
            print("Getting from cache")
            return storage[data]

        print("Calculating new result")
        result = func(*args, **kwargs)
        storage[data] = result
        return result

    return inner
