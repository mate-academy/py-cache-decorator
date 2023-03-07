def cache(func) -> dict:
    data_dict = {}
    def inner(*args):
        if args in data_dict:
            print("Getting from cache")
            return data_dict[args]
        else:
            print("Calculating new result")
            data_dict[args] = func(*args)
        return data_dict[args]
    return inner


@cache
def long_time_func(a,b,c):
    return(a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
