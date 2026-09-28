from typing import Callable, Any


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    # Створюємо ізольований словник кешу для кожної декорованої функції
    func_cache = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Створюємо унікальний ключ для комбінації аргументів.
        # Спочатку перетворюємо kwargs на кортеж з пар (ключ, значення)
        kwargs_key = tuple(sorted(kwargs.items()))
        cache_key = (args, kwargs_key)

        if cache_key in func_cache:
            print("Getting from cache")
            return func_cache[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        func_cache[cache_key] = result
        return result

    return wrapper
