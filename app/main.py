from typing import Callable, Any


def cache(func: Callable) -> Callable:
    list_for_result = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in list_for_result:
            print("Getting from cache")
            return list_for_result[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        list_for_result[key] = result
        return result
    return wrapper
