from functools import lru_cache

@lru_cache
def f(n):
	if n == 1:
		return 1
	else:
		return f(n-1) - 2*g(n-1)

@lru_cache
def g(n):
	if n == 1:
		return 1
	else:
		return f(n-1) + g(n-1) + n

print(sum([int(x) for x in str(g(36))]))