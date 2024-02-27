

def cache(func: callable) -> callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> int:
        if args in cache_dict:
            print("Getting from cache")
        else:
            cache_dict[args] = func(*args, **kwargs)
            print("Calculating new result")
        return cache_dict[args]

    return wrapper
