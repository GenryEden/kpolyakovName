def f(n):
	if n <= 3:
		return n
	elif n % 3 == 0:
		return n*n*n + f(n-1)
	elif n % 3 == 1:
		return 4+ f(n//3)
	else:
		return n*n + f(n-2)

print(f(100))