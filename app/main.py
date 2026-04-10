from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    _cache = {}  # окремий кеш для кожної функції

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # ключ з args та kwargs
        # для kwargs перетворюємо на кортеж відсортованих пар (ключ, значення)
        key = (args, tuple(sorted(kwargs.items())))

        if key in _cache:
            print("Getting from cache")
            return _cache[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        _cache[key] = result
        return result

    return wrapper
