def cache(func):
    d_memory = {}

    def inner(*args):
        if args in d_memory.keys():
            print("Getting from cache")
            return func(*args)
        else:
            d_memory[args] = func(*args)
            print("Calculating new result")
            return func(*args)
    return inner