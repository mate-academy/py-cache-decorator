def cache(func):
    save_value = {}

    def inner(*args, **kwargs):
        if args in save_value:
            print("Getting from cache")
            return save_value[args]
        res = func(*args, *kwargs)
        save_value[args] = res
        print("Calculating new result")
        return res
    return inner


@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple, power):
    return [number ** power for number in n_tuple]


@cache
def long_time_func_3(n_list, text):
    return f"{[i ** 2 for i in n_list]}, {text}"
