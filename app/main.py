def cache(func):
    cash_storage = {}

    def wrapper(*args):
        if args in cash_storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cash_storage[args] = func(*args)
        return cash_storage[args]
    return wrapper
