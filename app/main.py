def cache(func: int) -> None:
    rv = {}

    def wrapper(*args: int) -> None:
        if args in rv:
            print("Getting from cache")
            return rv[args]
        else:
            rv1 = func(*args)
            rv[args] = rv1
            print("Calculating new result")
            return rv[args]

    return wrapper
