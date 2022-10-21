def cache(func: callable) -> callable:
    cache_dict = {}

    def wrapper(*args) -> None:
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]
        if args not in cache_dict:
            print("Calculating new result")
            total = func(*args)
            cache_dict[args] = total
            return total
    return wrapper
