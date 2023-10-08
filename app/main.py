from typing import Callable


cache_history = dict()


def cache(func: Callable) -> Callable:
    def wrapper(*args) -> str:
        func_name = f"{func}({args})"

        if func_name in cache_history:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_history[func_name] = func(*args)

        return cache_history[func_name]

    return wrapper
