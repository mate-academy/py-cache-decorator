from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cash_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cash_dict:
            print("Getting from cache")
            return cash_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cash_dict[key] = result
            return result

    return wrapper
    pass
