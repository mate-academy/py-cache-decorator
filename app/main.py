def cache(func: callable) -> callable:
    dict_res = {}

    def inner(*args) -> callable:
        if args not in dict_res:
            res = func(*args)
            dict_res[args] = res
            print("Calculating new result")
            return dict_res[args]
        else:
            print("Getting from cache")
            return dict_res[args]
    return inner
