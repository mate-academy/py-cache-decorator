def cache(func: any) -> any:
    cache = {}

    def wrapper(*args) -> func:
        if args in cache:
            result = cache[args]
            print("Getting from cache")
        else:
            result = func(*args)
            cache[args] = result
            print("Calculating new result")
        return result
    return wrapper
