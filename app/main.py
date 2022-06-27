def cache(func):
    save_result = {}

    def inner(*args):
        if args not in save_result:
            result = func(*args)
            save_result[args] = result
            print("Calculating new result")
            return save_result[args]
        else:
            print("Getting from cache")
            return save_result[args]
    return inner


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
