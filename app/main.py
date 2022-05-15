import functools


def cache(func):
    memo = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in memo:
            print('Getting from cache')
            return memo[args]
        else:
            print("Calculating new result")
            rv = func(*args)
            memo[args] = rv
            return rv

    return wrapper


@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple, power):
    return [number ** power for number in n_tuple]
