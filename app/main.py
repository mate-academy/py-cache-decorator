def cache(func) -> None:
    cash_data = dict()

    def time_cashed(*args, **kwargs) -> str:
        if args not in cash_data:
            cash_data[args] = func(*args)
            print("Calculating new result")
        elif args in cash_data:
            print("Getting from cache")
        return cash_data[args]
    return time_cashed
