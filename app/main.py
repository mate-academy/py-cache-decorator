def cache(func):

    cached_list = []

    def inner(*args):

        element = list(args)

        for value in cached_list:
            if value == element:

                print("Getting from cache")

                for i in element:
                    return i

        print("Calculating new result")
        cached_list.append(element)

        return func(*args)
    return inner
