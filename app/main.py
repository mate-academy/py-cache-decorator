def cache(func):
    cash_storJ = {}

    def wrapper(*args):
        if args not in cash_storJ:
            print("Calculating new result")
            cash_storJ[args] = func(*args)
        else:
            print("Getting from cache")
        return cash_storJ[args]

    return wrapper
