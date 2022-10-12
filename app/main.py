def cache(func: any) -> any:
    cached_list = {}

    def inner(*args) -> any:
        if args in cached_list:

            cached_list[args] = "Getting from cache"
            print("Getting from cache")

            for item in args:
                return item

        cached_list[args] = "Calculating new result"
        print("Calculating new result")

        return func(*args)
    return inner
