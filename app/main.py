from typing import Any


def cache(func: callable) -> callable:
    previous_function_calls = {}

    def wrapper(*args) -> Any:
        if args not in previous_function_calls.keys():
            print("Calculating new result")
            previous_function_calls[args] = func(*args)
        else:
            print("Getting from cache")
        return previous_function_calls[args]
    return wrapper
