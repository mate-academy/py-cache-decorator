def cache(func):
    cache_lish = []

    def inner(*args, **kwargs):
        if args in cache_lish:
            print("Getting from cache")
            return func(*args, **kwargs)
        else:
            cache_lish.append(args)
            print("Calculating new result")
            return func(*args, **kwargs)

    return inner
