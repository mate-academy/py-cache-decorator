from functools import wraps
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    my_dict = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if args in my_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            my_dict[args] = func(*args, **kwargs)
        return my_dict[args]

    return wrapper
