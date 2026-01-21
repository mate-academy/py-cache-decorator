from typing import Callable, Any, Dict, Tuple


def cache(func: Callable) -> Callable:

    stored_results: Dict[Tuple[Any, ...], Any] = {}

    def wrapper(*args, **kwargs) -> Any:
        key = args + tuple(sorted(kwargs.items()))
        if key in stored_results:
            print("Getting from cache")
            return stored_results[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            stored_results[key] = result
            return result

    return wrapper


@cache
def long_time_func(aa: int, bb: int, cc: int) -> int:
    return (aa ** bb ** cc) % (aa * cc)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list[int]:
    return [number ** power for number in n_tuple]


if __name__ == "__main__":
    long_time_func(1, 2, 3)
    long_time_func(2, 2, 3)
    long_time_func_2((5, 6, 7), 5)
    long_time_func(1, 2, 3)
    long_time_func_2((5, 6, 7), 10)
    long_time_func_2((5, 6, 7), 10)
