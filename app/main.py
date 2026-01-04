from typing import Callable


def cache(func: Callable) -> Callable:
    save_result = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))
        if save_result.get(key, "no_save") != "no_save" :
            print("Getting from cache")

        else:
            save_result[key] = func(*args, **kwargs)
            print("Calculating new result")
        return save_result[key]
    return wrapper
