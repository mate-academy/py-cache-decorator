def cache(func: any) -> any:
    results = {}

    def inner(*args) -> str:
        if args in results.keys():
            print("Getting from cache")
            return results[args]
        print("Calculating new result")
        results.update({args: func(*args)})
        return results[args]

    return inner
