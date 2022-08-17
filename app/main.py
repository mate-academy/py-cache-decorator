def cache(func):
    cache_list = {}

    def wraper(*args, **kwargs):
        nonlocal cache_list
        if args in cache_list:
            print("Getting from cache")
            return cache_list[args]
        else:
            print("Calculating new result")
            new_value = func(*args)
            cache_list[args] = new_value
            return new_value
    return wraper


@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple, power):
    return [number ** power for number in n_tuple]
