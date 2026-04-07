from functools import wraps
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    # armazenamento do cache (por função)
    cache_storage = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        # 1) construir a chave a partir de args e kwargs
        key = (args, tuple(sorted(kwargs.items())))
        # 2) verificar se está no cache
        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]
        # 3) caso contrário: calcular resultado, armazenar, e retornar
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_storage[key] = result
        return result

    return wrapper
