from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    func_results = {}

    @wraps(func)
    def inner(*args) -> Any:
        if f"{args}" in func_results:
            print("Getting from cache")
        else:
            func_results[f"{args}"] = func(*args)
            print("Calculating new result")
        return func_results[f"{args}"]
    return inner
