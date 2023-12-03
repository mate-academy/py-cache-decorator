from functools import wraps
from typing import Any, Callable, Dict, Tuple

def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    results: Dict[Tuple[Any, ...], Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs) -> Any:
        print("Getting from cache" if args in results else "Calculating new result")
        return results.setdefault(args, func(*args))

    return wrapper
