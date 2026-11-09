from functools import wraps
from typing import Any, Callable


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    """Almacena resultados por función y argumentos inmutables."""

    cache_storage: dict[tuple[Any, ...], Any] = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[args]

        print("Calculating new result")
        result = func(*args)
        cache_storage[args] = result
        return result

    return wrapper
