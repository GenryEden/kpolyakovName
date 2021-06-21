def f(x):
	a = 0
	b = 1
	while x > 0:
		if x % 2 > 0:
			a += x % 12
		else:
			b *= x % 12
		x //= 12
	return a, b

for x in range(1, 1<<20):
	res = f(x)
	if res[0] == 7 and res[1] == 12:
		print(x)
		break