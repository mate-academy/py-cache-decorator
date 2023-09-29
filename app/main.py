from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    database = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if f"{args}, {kwargs}" in database.keys():
            print("Getting from cache")
        else:
            print("Calculating new result")
            database[f"{args}, {kwargs}"] = func(*args, **kwargs)
        return database[f"{args}, {kwargs}"]
    return wrapper
