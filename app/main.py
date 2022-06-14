def cache(func):
    total_list = []

    def inside(*args):
        for i in total_list:
            if args in i.keys():
                print("Getting from cache")
                return i[args]

        print("Calculating new result")
        result = func(*args)
        total_list.append({args: result})
        return result

    return inside


@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple, power):
    return [number ** power for number in n_tuple]
