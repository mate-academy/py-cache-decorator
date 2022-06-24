def cache(func):
    cache_memory = {}

    def wrapper(*args):
        if args not in cache_memory:
            print("Calculating new result")
            cache_memory[args] = func(*args)
        else:
            print("Getting from cache")
        return cache_memory[args]

    return wrapper
