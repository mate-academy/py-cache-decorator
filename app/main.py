def cache(func):

    cached_list = {}

    def inner(*args):

        for key, value in cached_list.items():
            if key == args:

                cached_list[args] = "Getting from cache"
                print(cached_list[args])

                for item in args:
                    return item





        cached_list[args] = "Calculating new result"
        print(cached_list[args])

        return func(*args)
    return inner
