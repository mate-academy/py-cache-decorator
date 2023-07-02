from typing import Callable, Any


def cache(func: callable) -> callable:
    data = {}

    def wrapper(*args: Any) -> Any:
        if args in data:
            print("Getting from cache")
            return data[args]
        print("Calculating new result")
        result = func(*args)
        data[args] = result
        return result
    
    return func
