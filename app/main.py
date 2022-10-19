def cache(func: object) -> object:
    cache = {}

    def wrapper(*args) -> str:
        if args in cache:
            result = cache[args]
            print("Getting from cache")
        else:
            result = func(*args)
            cache[args] = result
            print("Calculating new result")
        return result
    return wrapper
