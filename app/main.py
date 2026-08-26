from typing import Callable


def cache(func: Callable) -> Callable:
    count = {}

    def issue(*args, **kwargs) -> int:
        key = (args, tuple(sorted(kwargs.items())))
        if key in count:
            print("Getting from cache")
            return count[key]
        print("Calculating new result")
        value = func(*args, **kwargs)
        count[key] = value
        return value

    return issue
