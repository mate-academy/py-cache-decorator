def cache(func):
    cache_list = []

    def inner(*args, **kwargs):
        if args in cache_list:
            print("Getting from cache")
            return func(*args, **kwargs)
        else:
            cache_list.append(args)
            print("Calculating new result")
            return func(*args, **kwargs)

    return inner
