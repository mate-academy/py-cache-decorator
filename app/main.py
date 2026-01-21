from typing import Callable, Any, Tuple, Dict


def cache(func: Callable) -> Callable:
    # Словарь для хранения кэшированных результатов
    cache_dict: Dict[Tuple[Any, ...], Any] = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Создаем ключ для кэша на основе аргументов функции
        key = (args, frozenset(kwargs.items()))

        # Проверяем, есть ли результат в кэше
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            # Если результата нет в кэше, вычисляем его
            print("Calculating new result")
            result = func(*args, **kwargs)
            # Сохраняем результат в кэше
            cache_dict[key] = result
            return result

    return wrapper
