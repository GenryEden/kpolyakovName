def f(x):
	a = 0
	b = 1
	while x > 0:
		if x % 2 == 0:
			a += x % 13
		else:
			b *= x % 13
		x //= 13
	return a, b

for x in range(1, 1<<20):
	res = f(x)
	if res[0] == 5 and res[1] == 2:
		print(x)
		break