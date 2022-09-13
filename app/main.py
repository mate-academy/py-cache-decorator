def cache(func):
    cached_results = {}

    def wrapper(*args, **kwargs):
        if args in cached_results:
            print("Getting from cache")

        else:
            print("Calculating new result")
            cached_results[args] = func(*args, **kwargs)

        return cached_results[args]

    return wrapper
