def cache(func):
    cached_data = {}

    def wrap(*args):
        nonlocal cached_data
        for key, value in {args: func(*args)}.items():
            if str(key) not in cached_data:
                cached_data.update({f"{args}": func(*args)})
                print("Calculating new result")
                return cached_data[str(key)]
            else:
                print("Getting from cache")
                return cached_data[str(key)]
    return wrap


@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple, power):
    return [number ** power for number in n_tuple]
