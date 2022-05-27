def cache(func):
    cached_data = {}

    def wrap(*args):
        nonlocal cached_data
        if args in cached_data:
            print("Getting from cache")
            return cached_data[args]
        else:
            cached_data.update({args: func(*args)})
            print("Calculating new result")
            return cached_data[args]
    return wrap


@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple, power):
    return [number ** power for number in n_tuple]
