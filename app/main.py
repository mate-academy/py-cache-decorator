from functools import wraps
from typing import Any, Callable, Dict, Tuple


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    results: Dict[Tuple[Any, ...], Any] = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if args in results:
            print("Getting from cache")
        else:
            print("Calculating new result")
        return func(*args)
    return wrapper
