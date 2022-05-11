def cache(func):
    cache_dict = {}

    def inner(*args, **kwargs):
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[args] = result
        return result

    return inner


@cache
def sum(a, b):
    return a + b


@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple, power):
    return [number ** power for number in n_tuple]
