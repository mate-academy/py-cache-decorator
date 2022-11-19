from typing import Callable


def cache(func: Callable) -> Callable:
    input_data = {}

    def inner(*args, **kwargs) -> Callable:
        if args in input_data:
            print("Getting from cache")
        else:
            input_data.update({args: func(*args)})
            print("Calculating new result")
        return input_data[args]
    return inner
