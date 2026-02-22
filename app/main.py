from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    storage = {}

    @functools.wraps(func)
    def wrapper(*args : Any) -> Any:
        if args in storage:
            print("Getting from cache")
            return storage[args]
        print("Calculating new result")
        result = func(*args)

        # Зберігаємо результат у кеш
        storage[args] = result
        return result
    return wrapper
