def cache(func):
    saved = {}

    def inner(*args):
        func_with_args = (func, args)

        if func_with_args in saved:
            print("Getting from cache")
            return saved[func_with_args]

        print("Calculating new result")
        res = func(*args)
        saved[func_with_args] = res

        return res

    return inner
