def cache(func: callable) -> callable:
    cache_dct = {}

    def wrapped(*args) -> callable:
        if args in cache_dct:
            print("Getting from cache")
            return cache_dct[args]
        else:
            print("Calculating new result")
            total = func(*args)
            cache_dct[args] = total
            return total
    return wrapped
