from functools import lru_cache

@lru_cache
def f(n):
	if n == 1:
		return n
	else:
		return 2*f(n-1) + n + 3

print(f(19))