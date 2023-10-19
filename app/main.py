def cache(func: callable) -> callable:
    cached_results = dict()

    def wrapper(*args, **qwargs) -> callable:
        if args in cached_results:
            print("Getting from cache")
            return cached_results[args]
        else:
            print("Calculating new result")
            cached_results[args] = func(*args)
        return cached_results[args]
    return wrapper
