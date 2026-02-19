from typing import Callable


def cache(func: Callable) -> Callable:
    func_cache = {}

    def wrapper(*args) -> object:
        if args in func_cache:
            print("Getting from cache")
            return func_cache[args]
        else:
            print("Calculating new result")
            result = func(*args)
            func_cache[args] = result
            return result

    return wrapper


@cache
def long_time_func(first_number: int,
                   second_number: int,
                   third_number: int) -> int:
    return (first_number ** second_number ** third_number) % (
        first_number * third_number
    )


@cache
def long_time_func_2(numbers_tuple: tuple,
                     power_value: int) -> list[int]:
    return [number ** power_value for number in numbers_tuple]


if __name__ == "__main__":
    long_time_func(1, 2, 3)
    long_time_func(2, 2, 3)
    long_time_func_2((5, 6, 7), 5)
    long_time_func(1, 2, 3)
    long_time_func_2((5, 6, 7), 10)
    long_time_func_2((5, 6, 7), 10)
