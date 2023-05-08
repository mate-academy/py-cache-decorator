def cache(func: callable) -> callable:
    args_cache = {}

    def inner(*args) -> int:
        nonlocal args_cache
        if args in args_cache:
            print("Getting from cache")
            return args_cache[args]
        else:
            print("Calculating new result")
            result = func(*args)
            args_cache[args] = result
            return result
    return inner
