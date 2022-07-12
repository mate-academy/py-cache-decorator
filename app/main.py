def cache(func):
    cash_dict = {}

    def inner(*args, **kwargs):
        if args in cash_dict.keys():
            print("Getting from cache")
            return cash_dict[args]
        else:
            cash_dict[args] = func(*args, **kwargs)
            print("Calculating new result")
            return cash_dict[args]
    return inner
