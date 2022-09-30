def cache(func):

    cash_dict = {}

    def inner(*args, **kwargs):

        if args in cash_dict.keys():
            print("Getting from cache")
        else:
            print("Calculating new result")
            cash_dict[args] = func(*args, **kwargs)
        return cash_dict[args]

    return inner
