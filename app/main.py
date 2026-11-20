from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        # Створюємо унікальний ключ, який враховує і позиційні, і іменовані аргументи
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in cached_results:
            print("Getting from cache")
            return cached_results[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cached_results[cache_key] = result
        return result

    return wrapper

