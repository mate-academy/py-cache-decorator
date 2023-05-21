def cache(func):
    cash = {}

    def inner(*args, **kwargs):
        if args not in cash:
            print("Calculating new result")
            cash[args] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cash[args]
    return inner
