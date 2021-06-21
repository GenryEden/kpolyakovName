from functools import cache

@cache
def f(n):
	if n < 3:
		return n + 3
	elif n % 3 == 0:
		return (n + 2)*f(n-4)
	else:
		return n + f(n-1) + 2*f(n-2)

print(f(20))