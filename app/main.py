def cache(func):
    catche = {}

    def inner(*args):

        if args in catche:  # check previous results
            print("Getting from cache")
        else:
            # if result not in catch,
            # add result in cathc and return catch
            catche[args] = func(*args)
            print("Calculating new result")

        return catche[args]
    return inner
