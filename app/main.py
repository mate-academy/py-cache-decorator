def cache(func):
    cache_lib = {}

    def inner(*args):
        if args not in cache_lib:
            cache_lib[args] = func(*args)
            print('Calculating new result')
            return cache_lib[args]
        else:
            print('Getting from cache')
            return cache_lib[args]
    return inner
