def cache(func):
    data = {}

    def inner(*args, power: int = 0):
        if (args, power) in data:
            print("Getting from cache")
            return data[args, power]
        else:
            print("Calculating new result")
            if power == 0:
                data[args, power] = func(*args)
            else:
                data[args, power] = func(*args, power)
            return data[args, power]
    return inner
