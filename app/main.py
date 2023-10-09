from typing import Callable


def cache(func: Callable) -> Callable:
    cache_history = dict()

    def wrapper(*args) -> str:
        # func_name = f"{func}({args})"

        if f"{func}({args})" in cache_history:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_history[f"{func}({args})"] = func(*args)

        return cache_history[f"{func}({args})"]

    return wrapper
