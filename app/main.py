def cache(func):
    cash_repository = {}

    def wrapper(*args):
        if args not in cash_repository:
            print("Calculating new result")
            cash_repository[args] = func(*args)
        else:
            print("Getting from cache")
        return cash_repository[args]
    return wrapper
