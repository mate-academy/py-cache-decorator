from typing import Callable, Any


def cache(func: Callable) -> Any:
    all_number = []
    result = {}

    def check_data(*args: int) -> Callable:
        if args in all_number:
            print("Getting from cache")
        else:
            result[f"{func.__name__}{args}"] = func(*args)
            all_number.append(args)
            print("Calculating new result")
        return result[f"{func.__name__}{args}"]
    return check_data


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]


print(long_time_func_2((5, 6, 7), 5))
print(long_time_func_2((4, 7, 10), 10))
print(long_time_func_2((4, 7, 10), 10))
print(long_time_func(1, 2, 3))
print(long_time_func(2, 2, 3))
