def cache(func):
    cache_ = {}

    def wrapper(*args):
        if args in cache_:
            print("Getting from cache")
        else:
            cache_[args] = func(*args)
            print("Calculating new result")
        return cache_[args]
    return wrapper


@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple, power):
    return [number ** power for number in n_tuple]
