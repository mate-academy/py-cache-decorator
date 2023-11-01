from typing import Callable


def cache(func: Callable) -> Callable:
	cached_values = {}

	def inner(*args):
		if args in cached_values:
			print("Getting from cache")
		else:
			print("Calculating new result")
			cached_values[args] = func(*args)
		return cached_values[args]

	return inner
