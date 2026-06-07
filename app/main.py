from typing import Callable, Any

stored_results = {}


def cache(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        data = (func, args, tuple(kwargs.items()))
        if data in stored_results:
            print("Getting from cache")
            return stored_results.get(data)

        print("Calculating new result")
        result = func(*args, **kwargs)
        stored_results[data] = result
        return result
    return wrapper
