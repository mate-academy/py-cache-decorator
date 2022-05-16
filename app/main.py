def cache(func):
    cache_result = set()

    def wrapper(*args, **kwargs):
        if args not in cache_result:
            cache_result.add(args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return func(*args, *kwargs)

    return wrapper
