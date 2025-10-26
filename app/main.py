from typing import Callable, Any, Tuple, Dict


def cache(func: Callable) -> Callable[..., Any]:
    storage: Dict[Tuple[Any, ...], Any] = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key: Tuple[Any, ...] = args + tuple(sorted(kwargs.items()))
        if key in storage:
            print("Getting from cache")
            return storage[key]
        else:
            print("Calculating new result")
            result: Any = func(*args, **kwargs)
            storage[key] = result
            return result

    return wrapper
