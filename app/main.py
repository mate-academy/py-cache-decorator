from typing import Callable, Any, Tuple, List


def cache(func: Callable) -> Callable:
    saved_results = {}

    def wrapper(*args: Tuple[Any, ...]) -> Any:
        if args in saved_results:
            print("Getting from cache")
            return saved_results[args]

        print("Calculating new result")
        result = func(*args)
        saved_results[args] = result
        return result

    return wrapper


@cache
def long_time_func(base: int, exponent: int, modulo_factor: int) -> int:
    return (base ** exponent ** modulo_factor) % (base * modulo_factor)


@cache
def long_time_func_2(numbers: Tuple[int, ...], power: int) -> List[int]:
    return [number ** power for number in numbers]
