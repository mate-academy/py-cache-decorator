def cache(func: callable) -> callable:
    cache = {}

    def inner(*args) -> callable:
        if args in cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache[args] = func(*args)
        return cache[args]

    return inner
