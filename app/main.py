from typing import Callable, Any, Dict, Tuple


def cache(func: Callable) -> Callable:
    memo: Dict[Tuple[Any, ...], Any] = {}

    def wrapper(*args) -> Any:
        if args in memo:
            print("Getting from cache")
            return memo[args]
        print("Calculating new result")
        result = func(*args)
        memo[args] = result
        return result

    return wrapper
