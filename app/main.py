from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
     cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Створюємо ключ з аргументів
        key = (args, tuple(sorted(kwargs.items())))

        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cached_results[key] = result

        return result

    return wrapper
