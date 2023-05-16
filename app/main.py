from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    my_dict = {}

    def inner(*args, **kwargs) -> Any:
        if args not in my_dict:
            my_dict[args] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return my_dict[args]

    return inner
