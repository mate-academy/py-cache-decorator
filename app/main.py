def cache(func: callable) -> callable:
    res_dict = {}

    def inner(*args) -> int | float:
        if args in res_dict.keys():
            print("Getting from cache")
        else:
            res_dict[*args] = func(*args)
            print("Calculating new result")

        return res_dict[*args]

    return inner
