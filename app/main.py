from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    @wraps(func)
    def wrapped(*args, **kwargs) -> Any:
        function_name = f"{func.__name__}({args} {kwargs}"
        if function_name in cache_db:
            print("Getting from cache")
        else:
            cache_db.update({function_name: func(*args, **kwargs)})
            print("Calculating new result")
        return cache_db[function_name]

    return wrapped


cache_db = {}
