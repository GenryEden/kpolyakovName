def f(x):
	a = 0
	b = 10
	while x > 0:
		c = x % 10
		a += c
		if c < b:
			b = c
		x //= 10
	return a, b

for x in range(1, 1<<20):
	res = f(x)
	if res[0] == 13 and res[1] == 3:
		print(x)