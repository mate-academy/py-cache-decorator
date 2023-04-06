from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_args = [0]

    def wrapper(*args) -> Any:
        def check_cache(*args) -> bool:
            nonlocal cache_args
            for i in cache_args:
                if i != args:
                    continue
                print("Getting from cache")
                return True
            return False
        if check_cache(*args) is False:
            print("Calculating new result")
            cache_args.append(args)
            return func(*args)

    return wrapper


# @cache
# def long_time_func(a: int, b: int, c: int) -> int:
#     return (a ** b ** c) % (a * c)
#
#
# @cache
# def long_time_func_2(n_tuple: tuple, power: int) -> Any:
#     return [number ** power for number in n_tuple]
#
#
# long_time_func(1, 2, 3)
# long_time_func(2, 2, 3)
# long_time_func_2((5, 6, 7), 5)
# long_time_func(1, 2, 3)
# long_time_func_2((5, 6, 7), 10)
# long_time_func_2((5, 6, 7), 5)
# long_time_func_2((5, 6, 7), 10)
