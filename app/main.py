from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    cashed_dict = {}

    def inner(*args, **kwargs) -> Any:
        str_args = str(args)

        if str_args not in cashed_dict:
            result = func(*args, **kwargs)
            cashed_dict[str_args] = result
            print("Calculating new result")

            return result

        print("Getting from cache")
        return cashed_dict[str_args]

    return inner
