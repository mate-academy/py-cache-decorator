def cache(func: callable) -> callable:
    my_cache = dict()

    def wrapped_func(*args, **kwargs) -> callable:
        key = str(args) + str(kwargs)
        if key in my_cache:
            print("Getting from cache")
            return my_cache[key]
        value = func(*args, **kwargs)
        my_cache[key] = value
        print("Calculating new result")
        return value

    return wrapped_func


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
