def cache(func, *args, **kwargs):
    cache_dict = {}
    def wrapper(*spisok):
        if spisok in cache_dict:
            print("Getting from cache")
            return cache_dict.get(spisok)
        else:
            print("Calculating new result")
            result = func(*spisok)
            cache_dict[spisok] = result
            return result
    return wrapper

@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple, power):
    return [number ** power for number in n_tuple]

long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
