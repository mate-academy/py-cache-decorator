from typing import Callable


def cache(func):
    cache_dict = {}

    def wrapper(*args, **kwargs):
        # Тут потрібно створити ключ з args та kwargs
        # Пам'ятай: аргументи immutable, тому можемо використовувати їх як ключ
        key = args  # підказка: можна зробити tuple з args

        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[key] = result
        return result

    return wrapper
