def cache(func: object) -> object:
    cache = {}

    def wrapper(*args) -> str:
        signature = (func, *args)
        if signature in cache:
            result = cache[signature]
            print("Getting from cache")
        else:
            result = func(*args)
            cache[signature] = result
            print("Calculating new result")
        return result
    return wrapper
