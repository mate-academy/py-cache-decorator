from functools import wraps
from typing import Callable, Tuple, Dict, Any


def cache(func: Callable) -> Callable:
    tempe_big: Dict[Tuple] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        tempe_small = args + tuple(sorted(kwargs.items()))
        if tempe_small not in tempe_big:
            print("Calculating new result")
            tempe_big[tempe_small] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return tempe_big[tempe_small]

    return wrapper

