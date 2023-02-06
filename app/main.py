from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args) -> Callable:
        if f"{func.__name__}:{args}" in cache_dict:
            print("Getting from cache")
        else:
            cache_dict[f"{func.__name__}:{args}"] = func(*args)
            print("Calculating new result")
        return cache_dict.get(f"{func.__name__}:{args}")

    return wrapper
