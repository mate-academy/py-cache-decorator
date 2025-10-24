from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    func_cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        cache_key = args
        if cache_key in func_cache:
            print("Getting from cache")
            return func_cache[cache_key]
        else:
            # 3. Якщо результату немає, виконуємо функцію
            print("Calculating new result")
            result = func(*args, **kwargs)

            # 4. Зберігаємо результат у кеші перед поверненням
            func_cache[cache_key] = result
            return result

    return wrapper


@cache
def long_time_func(number1: int, number2: int, number3: int) -> int:
    return (number1 ** number2 ** number3) % (number1 * number3)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
