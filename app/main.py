def cache(func):
    cache_dict = {}

    def inner(*args):
        if args in cache_dict.keys():
            print("Getting from cache")
            return cache_dict[args]
        else:
            my_func = func(*args)
            cache_dict[args] = my_func
            print("Calculating new result")
            return my_func
    return inner


@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple, power):
    return [number ** power for number in n_tuple]
