from functools import wraps
from typing import Any, Callable, Dict, Tuple

def cache(func: Callable[..., Any], key_func: Callable[..., Tuple[Any, ...]] = None) -> Callable[..., Any]:
    results: Dict[Tuple[Any, ...], Any] = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        cache_key = key_func(*args) if key_func else args
        print("Getting from cache" if cache_key in results else "Calculating new result")
        return results.setdefault(cache_key, func(*args))

    return wrapper
