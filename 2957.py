def f(x):
	a = 0
	b = 1
	while x > 0:
		if x % 2 > 0:
			a += 1
		else:
			b += x % 5
		x //= 5
	return a, b

for x in range(100, 999+1):
	if f(x) == (2, 9):
		break

print(x)