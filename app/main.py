from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached = {}
    
    
    def wrapper(*args) -> Any:
        if args not in cached:
            print("Calculating new result")
            cached[args] = func(*args)
        else:
            print("Getting from cache")
        return cached[args]

    return wrapper
