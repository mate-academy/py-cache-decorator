def cache(func):
    # Write your code here
    pass
    ls = []

    def wrapper(*args, **kwargs):
        if args in ls:
            print("Getting from cache")
        else:
            ls.append(args)
            print("Calculating new result")
        return func(*args, **kwargs)
    return wrapper