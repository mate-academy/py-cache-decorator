from functools import wraps
from typing import Any, Callable, Dict, Tuple

def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    results: Dict[Tuple[Tuple[Any, ...], Dict[str, Any]], Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        cache_key = (args, frozenset(kwargs.items()))
        print("Getting from cache" if cache_key in results else "Calculating new result")
        return results.setdefault(cache_key, func(*args, **kwargs))

    return wrapper
