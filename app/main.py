from typing import Callable, Any
import inspect


def cache(func: Callable) -> Callable:
    memory_dict = {}
    sig = inspect.signature(func)  # получаем сигнатуру функции

    def inner(*args, **kwargs) -> Any:
        # связываем переданные аргументы с параметрами
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()  # подставляем значения по умолчанию
        key = tuple(bound.arguments.items())  # канонический ключ

        if key in memory_dict:
            print("Getting from cache")
            return memory_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            memory_dict[key] = result
            return result

    return inner
