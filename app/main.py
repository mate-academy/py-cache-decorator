def cache(func):
    cache_value: dict = {}

    def inner(*args):
        if cache_value.get(args) is None:
            print("Calculating new result")
            cache_value[args] = func(*args)
        else:
            print("Getting from cache")
        return cache_value.get(args)

    return inner