results = {}


def cache(func):
    global results

    def inner(*args):
        if func in results:
            if args in results[func] is not None:
                print("Getting from cache")
                return results[func][args]
        else:
            results[func] = {}

        print("Calculating new result")
        results[func][args] = func(*args)
        return results[func][args]

    return inner
