def f(x):
	a = 0
	b = 1
	while x > 0:
		if x % 2 > 0:
			a += x % 8
		else:
			b *= x % 8
		x //= 8
	return a, b

for x in range(999, 100-1, -1):
	res = f(x)
	if res == (2, 8):
		break

print(x)