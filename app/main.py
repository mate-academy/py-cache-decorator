from typing import Callable


def cache(func: Callable, *args, **kwargs) -> Callable:
    cache_dict = {}

    def wrapper(*new_list) -> Callable:
        if new_list in cache_dict:
            print("Getting from cache")
            return cache_dict.get(new_list)

        print("Calculating new result")
        result = func(*new_list)
        cache_dict[new_list] = result
        return result
    return wrapper


@cache
def long_time_func(first: int, second: int, third: int) -> int:
    return (first ** second ** third) % (first * third)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]


if __name__ == "__main__":
    long_time_func(1, 2, 3)
    long_time_func(2, 2, 3)
    long_time_func_2((5, 6, 7), 5)
    long_time_func(1, 2, 3)
    long_time_func_2((5, 6, 7), 10)
    long_time_func_2((5, 6, 7), 10)
