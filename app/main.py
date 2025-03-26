from functools import wraps


def cache(func):
    # Criação de um cache específico para cada função
    cache_storage = {}

    @wraps(func)
    def wrapper(*args, **kwargs):

        key = (func.__name__, args, frozenset(kwargs.items()))


        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]


        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_storage[key] = result
        return result

    return wrapper



@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


print(long_time_func(1, 2, 3))  # Calculando
print(long_time_func(2, 2, 3))  # Calculando
print(long_time_func_2((5, 6, 7), 5))  # Calculando
print(long_time_func(1, 2, 3))  # De cache
print(long_time_func_2((5, 6, 7), 10))  # Calculando
print(long_time_func_2((5, 6, 7), 10))  # De cache
