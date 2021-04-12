def f(n):
	a = -1
	while n > 7 and a != n % 8:
		a = n % 8
		n //= 8
	if a == n % 8:
		return a
	else:
		return n

for x in range(100, 1000):
	if f(x) == 5:
		print(x)
		break