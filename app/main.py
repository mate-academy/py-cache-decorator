from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}
    def inner(*args, **kwargs) -> None:
        key = (tuple(args)), tuple(sorted(kwargs.items()))
        if key in results:
            print("Getting from cache")
            return results[key]
        else:
            print("Calculating new result")
        result = func(*args, **kwargs)
        results[key] = result
        return result
    return inner

@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]

if __name__ == '__main__':
    long_time_func(1, 2, 3)
    long_time_func(2, 2, 3)
    long_time_func_2((5, 6, 7), 5)
    long_time_func(1, 2, 3)
    long_time_func_2((5, 6, 7), 10)
    long_time_func_2((5, 6, 7), 10)