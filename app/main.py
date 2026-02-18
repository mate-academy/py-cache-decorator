from typing import Callable, Any, Tuple


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    stored_results: dict[Tuple[Any, ...], Any] = {}

    def wrapper(*args: Any) -> Any:
        if args in stored_results:
            print("Getting from cache")
            return stored_results[args]

        print("Calculating new result")
        result = func(*args)
        stored_results[args] = result
        return result

    return wrapper
