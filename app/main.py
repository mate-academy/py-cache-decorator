from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = {}  # Кеш

    def wrapper(*args, **kwargs) -> Any:

        # Унікальний ключ на основі аргументів
        key = (args, tuple(sorted(kwargs.items())))

        if key not in results:
            print("Calculating new result")
            results[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return results[key]

    return wrapper
