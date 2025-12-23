from typing import Callable
from functools import wraps



def cache(func: Callable) -> Callable:
    container = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        func_key_name = func.__name__
        key = (args, tuple(sorted(kwargs.items()))) #yoben boben eto sho (ya pered cim taky func made OMG)

        if func_key_name not in container:
            container[func_key_name] = {}

        if key not in container[func_key_name]:
            print("Calculating new result")
            result = func(*args, **kwargs)
            container[func_key_name][key] = result
            return result
        else:
            print("Getting from cache")
            return container[func_key_name][key]

    return wrapper