from typing import Callable, Any


def cache(func: Callable) -> Callable:
    data = {}

    def inner(*args: Any) -> Any:
        nonlocal data
        param = args
        if param in data.keys():
            print("Getting from cache")
            return data[param]
        else:
            print("Calculating new result")
            new_result = func(*args)
            data[param] = new_result
            return new_result

    return inner
