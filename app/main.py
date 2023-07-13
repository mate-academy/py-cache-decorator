def cache(func: callable) -> callable:
    data = {}

    def wrapper(*args) -> callable:
        if args not in data:
            print("Calculating new result")
            res = func(*args)
            data[args] = res
        else:
            print("Getting from cache")
        return data[args]

    return wrapper
