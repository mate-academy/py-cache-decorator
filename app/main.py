from typing import Callable, Any


def cache(func: Callable) -> Callable:
    non_repeating_elements = {}

    def checking(*elements) -> Any:
        if elements not in non_repeating_elements:
            print("Calculating new result")
            non_repeating_elements[elements] = func(*elements)
        else:
            print("Getting from cache")
        return non_repeating_elements[elements]
    return checking