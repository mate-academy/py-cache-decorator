def cache(func):
    result_dict = {}

    def inner(*args):
        if args in result_dict:
            print('Getting from cache')
        else:
            print('Calculating new result')
            result_dict[args] = func(*args)
        return result_dict[args]
    return inner


@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple, power):
    return [number ** power for number in n_tuple]
