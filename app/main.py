def cache(func):
    cache_dict = {}

    def wrapper1(*args):
        if args not in cache_dict:
            cache_dict[args] = func(*args)
            print("Calculating new result")
            return cache_dict[args]
        else:
            print("Getting from cache")
            return cache_dict[args]
    return wrapper1


@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple, power):
    return [number ** power for number in n_tuple]