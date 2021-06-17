def f(x):
	a = 0
	b = 0
	while x > 0:
		a += 1
		if x % 2 == 0:
			b += x % 10
		x //= 10
	return a, b

for x in range(1, 1<<20):
	res = f(x)
	if res[0] == 3 and res[1] == 18:
		print(x)
		break