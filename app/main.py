def cache(func: callable) -> callable:
    cache_dct = {}

    def wrapped(*args) -> callable:
        if args in cache_dct:
            print("Getting from cache")
        else:
            print("Calculating new result")
            total = func(*args)
            cache_dct[args] = total
        return cache_dct[args]
    return wrapped
