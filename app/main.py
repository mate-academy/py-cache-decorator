def cache(func):
    cached_list = []

    def inner(*args):
        access = True
        element = list(args)

        if cached_list:
            for value in cached_list:
                if value == element:

                    print("Getting from cache")
                    access = False

        if access:

            print("Calculating new result")
            cached_list.append(element)

        else:
            for value in element:

                return value

        return func(*args)
    return inner
    pass
