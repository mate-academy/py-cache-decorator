from typing import Callable


def cache(func: Callable) -> Callable:
    calculated_data = {}

    def inner(*args) -> int:
        if args not in calculated_data:
            print("Calculating new result")
            calculated_data[args] = func(*args)
            return calculated_data[args]
        print("Getting from cache")
        return calculated_data[args]

    return inner
