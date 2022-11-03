def cache(func: callable) -> callable:
    dict_cache = {}

    def wrapper(*args) -> callable:

        if args in dict_cache:
            print("Getting from cache")
            return dict_cache[args]
        dict_cache[args] = func(*args)
        print("Calculating new result")

        return dict_cache[args]
    return wrapper
