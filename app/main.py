from typing import Callable, Any


def cache(func: Callable) -> Callable:
    story = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in story:
            print("Getting from cache")
            return story[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        story[key] = result
        return result
    return wrapper


@cache
def long_time_func(number_one: int, number_two: int, number_three: int) -> int:
    return ((number_one ** number_two ** number_three)
            % (number_one * number_three))


@cache
def long_time_func2(number_1: int, number_2: int, number_3: int) -> int:
    return ((number_1 ** number_2 ** number_3)
            % (number_1 * number_3))
