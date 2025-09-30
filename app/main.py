from typing import Callable

def cache(func: Callable) -> Callable:
    """
    A decorator that caches the results of a function call.
    """
    # 1. Створюємо "сховище" для результатів. Це словник.
    cache_storage = {}

    def wrapper(*args):
        # 2. Перевіряємо, чи результат для цих аргументів вже є в кеші.
        # Аргументи 'args' будуть ключем у нашому словнику.
        if args in cache_storage:
            # 3. Якщо так, повертаємо збережений результат, не викликаючи функцію.
            print(f"Returning from cache for args: {args}")
            return cache_storage[args]
        else:
            # 4. Якщо ні, то викликаємо оригінальну функцію.
            print(f"Calculating for args: {args}")
            result = func(*args)
            
            # 5. Зберігаємо новий результат у кеш.
            cache_storage[args] = result
            
            # 6. Повертаємо цей новий результат.
            return result

    # Декоратор повертає нашу нову функцію-обгортку.
    return wrapper

# --- Приклад використання (можете додати це для перевірки) ---

@cache
def slow_sum(a: int, b: int) -> int:
    """A function that simulates a slow calculation."""
    # Уявімо, що ця функція працює дуже довго
    return a + b

# Перший виклик з аргументами (2, 3)
print(slow_sum(2, 3))
print("-" * 20)

# Другий виклик з тими ж аргументами (2, 3)
print(slow_sum(2, 3))
print("-" * 20)

# Перший виклик з новими аргументами (5, 4)
print(slow_sum(5, 4))