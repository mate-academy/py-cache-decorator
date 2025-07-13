from typing import Callable, Any, Dict, Tuple


def cache(func: Callable) -> Callable:
    cashe_store: Dict[Tuple[Any, ...], Any] = {}
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cashe_store:
            print("Getting from cache")
            return cashe_store[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cashe_store[key] = result
            return result

    return wrapper
