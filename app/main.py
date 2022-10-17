def cache(func):
    cache_dict = {}

    def wrapper(*args):
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]
        cache_dict[args] = func(*args)
        print("Calculating new result")
        return cache_dict[args]
    return wrapper


@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple, power):
    return [number ** power for number in n_tuple]
