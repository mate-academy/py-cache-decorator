from typing import Callable, TypeVar, Any

FuncT = TypeVar("FuncT", bound=Callable[..., Any])


def cache(func: FuncT) -> FuncT:
    cache_dict: dict[tuple, Any] = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(kwargs.items()))
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result

    return wrapper
