def cache(func):
    # Write your code here
    cache_storage = {}

    def inner(*args):
        if args in cache_storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_storage[args] = func(*args)

        return cache_storage[args]

    return inner
