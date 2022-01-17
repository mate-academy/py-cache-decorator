def cache(func):

    memory = {}

    def wrapper(*args):

        if args in memory:
            print("Getting from cache")

        else:
            memory[args] = func(*args)
            print("Calculating new result")

        return memory[args]
    return wrapper
