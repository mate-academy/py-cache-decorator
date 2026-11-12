from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar

# Використовуємо довшу назву замість 'F', щоб задовольнити VNE001
FuncT = TypeVar("FuncT", bound=Callable[..., Any])


def cache(func: FuncT) -> FuncT:
    # Словник для зберігання результатів окремо
    # для кожної декорованої функції
    results_cache: dict[tuple[Any, ...], Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Оскільки словники та списки є змінними (mutable),
        # перетворюємо всі аргументи на незмінні типи (кортежі
        # з'єднаних пар для kwargs), щоб їх можна було
        # використати як ключі словника (hashable).
        kwargs_items = tuple(sorted(kwargs.items()))
        cache_key = (args, kwargs_items)

        # Перевіряємо, чи є вже збережений результат
        # для цих аргументів у цій функції
        if cache_key in results_cache:
            print("Getting from cache")
            return results_cache[cache_key]

        # Якщо результату немає, обчислюємо його
        print("Calculating new result")
        result = func(*args, **kwargs)

        # Зберігаємо результат у кеші для подальшого використання
        results_cache[cache_key] = result
        return result

    return wrapper  # type: ignore[return-value]
