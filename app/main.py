def cache(func):
    saved = {}

    def inner(*args):
        if args in saved:
            print("Getting from cache")

            return saved[args]

        print("Calculating new result")
        res = func(*args)
        saved[args] = res

        return res

    return inner
