def cache(func):
    result_old_task = {}

    def inner(*args):
        if args in result_old_task:
            print("Getting from cache")
            return result_old_task[args]

        else:
            result = func(*args)
            result_old_task.update({args: result})
            print("Calculating new result")
            return result

    return inner
