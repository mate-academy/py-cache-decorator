from typing import Any, Callable


def cache(func: Callable) -> Callable:
    stored_results: dict[tuple[Any, ...], Any] = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
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
def long_time_func(first_num: int, second_num: int, third_num: int) -> int:
    return (first_num ** second_num ** third_num) % (first_num * third_num)


@cache
def long_time_func_2(n_tuple: tuple[int, ...], power: int) -> list[int]:
    return [number ** power for number in n_tuple]
