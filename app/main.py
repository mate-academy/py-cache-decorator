def cache(func):

    c = func.__name__
    global cash_dict
    cash_dict = {}

    def inner(*args, **kwargs):

        nonlocal c
        result = str([item for item in args])
        result += c
        if result in cash_dict.keys():
            print("Getting from cache")
        else:
            print("Calculating new result")
            cash_dict[result] = func(*args, **kwargs)
        return cash_dict[result]

    return inner
