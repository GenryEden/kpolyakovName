def f(n):
	if n < 5:
		return f(3*n) + f(n + 3) + f(n + 1)
	else:
		return n // 2

print(f(2))