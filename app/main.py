from functools import wraps


def cache(func: callable) -> callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args: tuple, **kwargs: dict) -> any:
        key = args + tuple(kwargs.items())
        if key not in cache_dict:
            cache_dict[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_dict[key]

    return wrapper


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
