def cache(func):
    total_dict = {}

    def inside(*args):
        if args in total_dict.keys():
            print("Getting from cache")
            return total_dict[args]

        print("Calculating new result")
        result = func(*args)
        total_dict[args] = result
        return result

    return inside


@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple, power):
    return [number ** power for number in n_tuple]
