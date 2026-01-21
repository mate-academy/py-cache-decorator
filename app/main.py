from typing import Callable, Any


def cache(func: Callable) -> Callable:
    data = {}

    def wrapper(*args, **kwargs) -> Any:
        key = args + tuple(kwargs.items())

        if key in data:
            print("Getting from cache")
            return data[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        data.update({key: result})
        return result

    return wrapper
