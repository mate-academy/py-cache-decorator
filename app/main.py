from typing import Callable, Any, Dict, Tuple


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    results: Dict[Tuple[Any, Any], Any] = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in results:
            print("Getting from cache")
            return results[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        results[cache_key] = result
        return result

    return wrapper


@cache
def long_time_func(num_a: int, num_b: int, num_c: int) -> int:
    return (num_a ** num_b ** num_c) % (num_a * num_c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
