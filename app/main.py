from typing import Callable, Any, Dict, Tuple
from functools import wraps


def cache(func: Callable) -> Callable:
    # Storage is initialized here to be captured by the wrapper function (closure).
    storage: Dict[Tuple, Any] = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:

        # 1. Creating a single, hashable key for caching:
        kwargs_tuple = tuple(sorted(kwargs.items()))
        key = (args, kwargs_tuple)

        # 2. Caching logic
        if key in storage:
            # Оновлено: Виводиться лише 'Getting from cache'
            print("Getting from cache")
            return storage[key]
        else:
            # Оновлено: Виводиться лише 'Calculating new result'
            print("Calculating new result")
            res = func(*args, **kwargs)
            storage[key] = res
            return res

    return wrapper


# --- Приклад використання (для перевірки) ---

@cache
def multiply(a: int, b: int) -> int:
    return a * b


print("Виклик 1:")
multiply(2, 3)

print("Виклик 2:")
multiply(2, 3)