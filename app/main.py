from functools import wraps
from typing import Any, Callable


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    """Almacena resultados por función y argumentos inmutables."""

    cache_storage: dict[tuple[tuple[Any, ...], tuple[tuple[str, Any], ...]], Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_storage[key] = result
        return result

    return wrapper

