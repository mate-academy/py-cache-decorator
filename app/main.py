def cache(func: callable) -> callable:
    cache_lib = {}

    def inner(*args) -> callable:
        nonlocal cache_lib
        if args not in cache_lib:
            cache_lib[args] = func(*args)
            print("Calculating new result")
            return cache_lib[args]
        if args in cache_lib:
            print("Getting from cache")
            return cache_lib[args]
    return inner
