from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    hash_table = {}

    def inner(*args: Any) -> None:
        key = str(args)
        if key in hash_table:
            print("Getting from cache")
        else:
            print("Calculating new result")
            hash_table[key] = func(*args)
        return hash_table[key]
    return inner
