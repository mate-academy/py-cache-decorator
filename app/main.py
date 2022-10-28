def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args) -> Callable:
        if args in cache:
            result = cache[args]
            print("Getting from cache")
        else:
            result = func(*args)
            cache[args] = result
            print("Calculating new result")
        return result
    return wrapper
