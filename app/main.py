from typing import Callable, Any, Tuple, Dict


def cache(func: Callable) -> Callable[[tuple[Any, ...], dict[str, Any]], Any]:
    cached_results = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if args in cached_results:
            print("Getting from cache")
            return cached_results[args]
        else:
            result = func(*args, **kwargs)
            cached_results[args] = result
            print("Calculating new result")
            return result

    return wrapper