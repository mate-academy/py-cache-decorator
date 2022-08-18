def cache(func):
    d_memory = {}

    def inner(*args):
        if args in d_memory.keys():
            print("Getting from cache")
            return d_memory[args]
        d_memory[args] = func(*args)
        print("Calculating new result")
        return d_memory[args]
    return inner
