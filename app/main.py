from typing import Callable


def cache(func: Callable) -> Callable:
    cashed_data = {}

    def wrapper(*args, **kwargs) -> Callable:
        cashed_key = tuple(args)

        if cashed_key in cashed_data:
            print("Getting from cache")
            return cashed_data[cashed_key]
        else:
            data = func(*args, **kwargs)
            cashed_data[cashed_key] = data
            print("Calculating new result")
            return data

    return wrapper
