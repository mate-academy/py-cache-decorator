from typing import Callable, Any


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    func_cache = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(kwargs.items()))

        if key in func_cache:
            print("Getting from cache")
            return func_cache[key]

        func_cache[key] = func(*args, **kwargs)
        print("Calculating new result")
        return func_cache[key]

    return wrapper
