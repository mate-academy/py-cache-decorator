from typing import Callable, Any


def cache(func: Callable) -> Callable:
    mass = {}
    def wrapper(*args, **kwargs) -> Any:
        if args in mass:
            print("Getting from cache")
            return mass[args]
        else:
            print("Calculating new result")
            mass[args] = func(*args, **kwargs)
            return mass[args]
    return wrapper
    