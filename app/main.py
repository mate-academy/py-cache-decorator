from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def inner(*args, **kwargs) -> int:
        data = (args, tuple(sorted(kwargs.items())))
        result = 0

        for arg in data:
            if arg:
                if arg not in storage:
                    print("Calculating new result")
                    result = func(*args, **kwargs)
                    storage[arg] = result
                else:
                    print("Getting from cache")
                    result = storage[arg]

        return result

    return inner
