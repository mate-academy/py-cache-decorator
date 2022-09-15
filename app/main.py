def cache(func):
    cash_storj = {}

    def wrapper(*args):
        if args not in cash_storj:
            print("Calculating new result")
            cash_storj[args] = func(*args)
        else:
            print("Getting from cache")
        return cash_storj[args]

    return wrapper
