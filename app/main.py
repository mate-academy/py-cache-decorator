def cache(func):
    caches = ()

    def inner(*args):
        nonlocal caches

        if len(args) == 3:
            (a, b, c) = args
            cache = func(a, b, c)
        if len(args) == 2:
            cache = func(args[0], args[1])

        if cache in caches:
            print("Getting from cache")
            return cache
        else:
            print("Calculating new result")
            caches += (cache,)
            return cache
    return inner


@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple, power):
    return [number ** power for number in n_tuple]


long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
