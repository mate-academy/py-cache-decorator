from typing import Callable


def cache(func: Callable) -> Callable:
    save_cache = {}

    def wrapper(*args, **kwargs) -> Callable[[callable], callable]:
        key = (args, tuple(sorted(kwargs.items())))

        if key in save_cache:
            print("Getting from cache")
            return save_cache[key]

        result = func(*args, **kwargs)
        save_cache[key] = result
        print("Calculating new result")

        return result
    return wrapper
