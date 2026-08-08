from functools import wraps
from typing import Callable, Any

def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    func_cache: dict = {}
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in func_cache:
            print("Getting from cache")
            return func_cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            func_cache[key] = result
            return result
    return wrapper

