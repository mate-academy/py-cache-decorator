def cache(func: tuple) -> str:
    archive = {}

    def inner(*args, **kwargs) -> None:
        if args not in archive:
            result = func(*args, **kwargs)
            archive[args] = result
            print("Calculating new result")
        else:
            print("Getting from cache")
        return archive[args]
    return inner
