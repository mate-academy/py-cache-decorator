def cache(func):
    results = {}

    def inner(*args):
        if args not in results:
            results[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return results[args]
    return inner


@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple, power):
    return [number ** power for number in n_tuple]
