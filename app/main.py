def cache(func):
    save_value = {}

    def inner(*args, **kwargs):
        if args in save_value:
            print("Getting from cache")
            return save_value[args]
        res = func(*args, *kwargs)
        save_value[args] = res
        print("Calculating new result")
        return res
    return inner
