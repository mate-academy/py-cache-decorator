from typing import Callable

func_cache_storage = {}


def cache(func: Callable) -> type(Callable):

    if func not in func_cache_storage:
        func_cache_storage[func] = {}

    current_func_cache = func_cache_storage[func]

    def wrapper(*args) -> type(Callable):
        key = args

        if key in current_func_cache:
            print("Getting from cache")
            return current_func_cache[key]
        else:
            print("Calculating new result")
            result = func(*args)
            current_func_cache[key] = result
            return result

    return wrapper
