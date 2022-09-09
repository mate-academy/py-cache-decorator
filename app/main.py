def cache(func):
    cash_data = dict()

    def time_cashed(*args, **kwargs):
        if args not in cash_data:
            cash_data[args] = func(*args)
            print('Calculating new result')
            return cash_data[args]
        elif args in cash_data:
            print('Getting from cache')
            return cash_data[args]
    return time_cashed
