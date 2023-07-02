from typing import Callable, Any


def cache(func: callable) -> callable:
    data = {}

    def wrapper(*args: Any) -> Any:
        if args in data:
            print("Getting from cache")
            return data[args]
        print("Calculating new result")
        data[args] = func(*args)
        return func(*args)
    
    return func
