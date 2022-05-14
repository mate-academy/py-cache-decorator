def cache(func):
    cache_storage = {}

    def inner(*args):
        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[args]
        else:
            print("Calculating new result")
            res = func(*args)
            cache_storage[args] = res
            return res

    return inner
