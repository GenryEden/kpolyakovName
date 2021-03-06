from functools import cache

@cache
def f(n):
	if n < 10:
		return n
	else:
		return f(g(n))

@cache
def g(n):
	if n < 10:
		return n
	else:
		return n % 10 + g(n // 10)

print(f(12345678987654321))