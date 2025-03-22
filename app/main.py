import functools

def cache(func):
    func_cache = {}  # Cache specific to this decorated function

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items()))) # Create a key from args and kwargs

        if key in func_cache:
            print("Getting from cache")
            return func_cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            func_cache[key] = result
            return result

    return wrapper

@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]

long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)