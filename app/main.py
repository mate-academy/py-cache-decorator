from typing import Callable, Any
from functools import wraps


def make_hashable(value: Any) -> Any:
    if isinstance(value, list):
        converted_items = []
        for item in value:
            converted_items.append(make_hashable(item))
        return tuple(converted_items)

    if isinstance(value, dict):
        converted_items = []
        for key, value in value.items():
            converted_items.append((key, make_hashable(value)))
        return tuple(sorted(converted_items))

    if isinstance(value, set):
        converted_items = []
        for item in value:
            converted_items.append(make_hashable(item))
        return tuple(sorted(converted_items))

    return value


def cache(func: Callable) -> Callable:
    memory = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        safe_args_list = []
        for arg in args:
            safe_args_list.append(make_hashable(arg))
        safe_args = tuple(safe_args_list)

        safe_kwargs_list = []
        for key, value in kwargs.items():
            safe_kwargs_list.append((key, make_hashable(value)))
        safe_kwargs = tuple(sorted(safe_kwargs_list))

        key = (safe_args, safe_kwargs)

        if key in memory:
            print("Getting from cache")
            return memory[key]

        print("Calculating new result")
        result = func(*args, **kwargs)

        memory[key] = result
        return result

    return wrapper
