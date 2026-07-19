from collections.abc import Callable
from functools import wraps
from typing import Any


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that caches results of a function for previously seen
    (hashable/immutable) arguments, so repeated calls with the same
    arguments don't re-run the function body.

    Each decorated function gets its own, independent cache store.
    """
    stored_results: dict[tuple[Any, ...], Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Build a single hashable key from both positional and keyword args.
        # kwargs are sorted by key so that call order doesn't affect the key.
        key = (args, tuple(sorted(kwargs.items())))

        if key in stored_results:
            print("Getting from cache")
            return stored_results[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        stored_results[key] = result
        return result

    return wrapper


@cache
def long_time_func(base: int, exponent: int, modifier: int) -> int:
    return (base ** exponent ** modifier) % (base * modifier)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]


if __name__ == "__main__":
    long_time_func(base=1, exponent=2, modifier=3)
    long_time_func(base=2, exponent=2, modifier=3)
    long_time_func_2((5, 6, 7), 5)
    long_time_func(base=1, exponent=2, modifier=3)
    long_time_func_2((5, 6, 7), 10)
    long_time_func_2((5, 6, 7), 10)

    # Expected output:
    # Calculating new result
    # Calculating new result
    # Calculating new result
    # Getting from cache
    # Calculating new result
    # Getting from cache
