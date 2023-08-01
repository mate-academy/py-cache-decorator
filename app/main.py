from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    memory = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        if args in memory:
            print("Getting from cache")
            return memory.get(args)
        res = func(*args, **kwargs)
        memory[args] = res
        print("Calculating new result")
        return res
    return inner
