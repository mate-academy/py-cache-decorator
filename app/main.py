from typing import Callable, Any


def cache(func: Callable) -> Callable:
    data = {}
    result_history = {}

    def inner(*args: Any) -> Any:
        nonlocal data
        nonlocal result_history
        param = args
        if param in data.keys():
            print("Getting from cache")
            return result_history[param]
        else:
            print("Calculating new result")
            new_result = func(*args)
            data[param] = param
            result_history[param] = new_result
            return new_result

    return inner
