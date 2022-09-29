def cache(func):

    c = func.__name__
    cash_dict = {}

    def inner(*args, **kwargs):

        nonlocal c
        result = args + tuple(c)
        if result in cash_dict.keys():
            print("Getting from cache")
        else:
            print("Calculating new result")
            cash_dict[result] = func(*args, **kwargs)
        return cash_dict[result]

    return inner
