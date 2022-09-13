def cache(func):
    memory = {}

    def wrapper(*args):
        if args in memory:
            print("Getting from cache")
        else:
            print("Calculating new result")
            memory[args] = func(*args)

        return memory[args]

    return wrapper
