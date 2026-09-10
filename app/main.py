from typing import Callable


def cache(func: Callable) -> Callable:

    result_storage = {}

    def wrapper(*args, **kwargs) -> int:

        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in result_storage:
            print("Getting from cache")
            return result_storage[cache_key]
        else:
            # Зберігаємо результат за новим комплексним ключем
            result_storage[cache_key] = func(*args, **kwargs)
            print("Calculating new result")
            return result_storage[cache_key]
    return wrapper
