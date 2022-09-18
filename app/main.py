def cache(func):
    new_dict = {}

    def inner(*args, **kwargs):
        if args not in new_dict:
            new_dict[args] = func(*args)
            print("Calculating new result")

        else:
            print("Getting from cache")
        return new_dict.get(args)
    return inner


@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a * c)


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func(1, 2, 3)
