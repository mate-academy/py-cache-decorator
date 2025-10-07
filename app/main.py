from typing import Callable, Any


def cache(func: Callable) -> Callable:
    # Кеш створюється тут, доступний через замикання
    cache_store = {}

    # 1. wrapper приймає будь-яку кількість аргументів
    def wrapper(*args, **kwargs) -> Any:

        # 2. Обробка ключових аргументів (kwargs)
        sorted_kwargs = tuple(sorted(kwargs.items()))

        # 3. Створення фінального хешованого ключа
        key = (args, sorted_kwargs)

        if key in cache_store:  # Використовуємо cache_store
            # Cache Hit: Беремо з кешу
            print("Getting from cache")
            return cache_store[key]
        else:
            # Cache Miss: Викликаємо оригінальну функцію
            result = func(*args, **kwargs)
            cache_store[key] = result  # Зберігаємо в кеш
            print("Calculating new result")
            return result

    return wrapper  # Повертаємо обгортку (wrapper)


@cache
def long_time_func(a_var: int, b_var: int, c_var: int) -> int:
    return (a_var ** b_var ** c_var) % (a_var * c_var)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)  # Cache Hit
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)  # Cache Hit
