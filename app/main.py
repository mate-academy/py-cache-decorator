def cache(func):
    caches = []

    def inner(*args):
        local_cache = []
        for arg in args:
            local_cache.append(arg)
        if local_cache in caches:
            print("Getting from cache")
        else:
            print("Calculating new result")
            caches.append(local_cache)

        return func(*args)

    return inner


@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple, power):
    return [number ** power for number in n_tuple]
