from typing import Callable, Any
import inspect


def cache(func: Callable) -> Callable:
    bufor = {}
    sig = inspect.signature(func)

    def wrapper(*args, **kwargs) -> Any:
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()
        key = tuple(bound.arguments.items())
        if key in bufor:
            print("Getting from cache")
            return bufor[key]
        else:
            print("Calculating new result")
            bufor[key] = func(*args, **kwargs)
            return bufor[key]

    return wrapper
