from typing import Any, Callable


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    cache_dict: dict[tuple[Any, ...], Any] = {}

    def wrapper(*args: Any) -> Any:
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]
        print("Calculating new result")
        cache_dict[args] = func(*args)
        return cache_dict[args]

    return wrapper
