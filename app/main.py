from typing import Callable


def cache(func: Callable) -> Callable:
    diсtant = {}

    def inner(*args, **kwargs) -> Callable:
        tuple_of_numbers = (args, tuple(kwargs.items()))
        if tuple_of_numbers in diсtant:
            print("Getting from cache")
            return diсtant[tuple_of_numbers]
        else:
            print("Calculating new result")
            diсtant[tuple_of_numbers] = func(*args, **kwargs)
            return diсtant[tuple_of_numbers]

    return inner
