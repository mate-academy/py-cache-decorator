from typing import Callable, Any


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    # Словник для зберігання результатів конкретної функції
    results: dict[tuple[Any, ...], Any] = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Створюємо унікальний ключ із позиційних та іменованих аргументів
        # Перетворюємо kwargs у кортеж пар (ключ, значення), щоб він став hashable
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in results:
            print("Getting from cache")
            return results[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        results[cache_key] = result
        return result

    return wrapper


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
