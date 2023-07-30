from typing import Callable, Any


def cache(func: Callable) -> Any:
    memory = {}

    def inner(*args) -> str:
        if args in memory:
            print("Getting from cache")
            return memory.get(args)
        else:
            res = func(*args)
            memory[args] = res
            print("Calculating new result")
            return res
    return inner
