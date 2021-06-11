from functools import cache

@cache
def f(n):
	if n < 10:
		return n
	else:
		return n % 10 + f(n//10)

@cache
def g(n):
	if n < 10:
		return n
	else:
		return g(f(n))
s = 0
for n in range(10, 100):
	s += g(n)
print(s)