def cache(func: callable) -> callable:
    cached = {}

    def inner(*args: int | float) -> int | list:
        if args not in cached.keys():
            print("Calculating new result")
            result = func(*args)
            cached[args] = result
            return result
        else:
            print("Getting from cache")
            return cached[args]

    return inner
